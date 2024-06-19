AUDIT (
  name assert_notnull_codes,
);

SELECT *
FROM @this_model
WHERE
  @column is null
