import textwrap
from datetime import datetime, timedelta

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator

with DAG(
    "test",
    default_args={
        "depends_on_past": False,
        "email" : ["contact@pragmatias.fr"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description = "A simple test with a DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2024,5,14),
    catchup=False,
    tags=["test","poc"],
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )
    
    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )
    
    t1.doc_md = textwrap.dedent(
        """\
        #### Task Documentation
        testing doc 
        """
    )

    dag.doc_md = __doc__
    dag.doc_md = """
    This is a documentation testing
    """

    templated_command = textwrap.dedent(
        """
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7)}}"
        {% endfor %}
        """
    )

    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command,
    )


    t2 >> t1 >> t3
