{% test is_positive(model, column_name) %}

with validation as (
    select {{ column_name }} as nbr
    from {{ model }}
)

select *
from validation
-- get all negative data
where nbr < 0


{% endtest %}