-- A SQL script that lists all bands with "Glam rock"
-- ranked by theire longevity.
SELECT 
    band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM 
    metal_bands
WHERE
    style
LIKE
    '%Glam rock%'
;