with cities as (
    select insee_code
        ,nom
        ,zip_code
        ,department_number
        ,department_name
        ,latitude
        ,longitude
        ,population
        ,row_number over (partition by zip_code order by population desc) as placement
    from {{ ref('ref_cities') }}
)

select *
from cities
where placement <= 5
order by placement
