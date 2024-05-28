select code
    ,population
from {{ ref('communes') }}
where population < 0