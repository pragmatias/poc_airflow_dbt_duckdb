AUDIT (
  name assert_positive_geonameid,
);

SELECT *
FROM @this_model
WHERE
  geonameid < 0
