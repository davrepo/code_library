-- (a)
SELECT COUNT(*)
FROM chefs
WHERE id NOT IN (
    SELECT created_by
    FROM recipes
);

-- (b)
SELECT COUNT(DISTINCT recipes.id)
FROM master
JOIN chefs ON master.chef_id = chefs.id
JOIN recipes ON master.recipe_id = recipes.id
JOIN use ON recipes.id = use.recipe_id
JOIN ingredients ON use.ingredient_id = ingredients.id
WHERE chefs.name = 'Spicemaster' AND ingredients.type = 'spice'
GROUP BY chefs.id;

-- (c)
select count(*)
from recipes
where id not in (
	select S.recipe_id
	from steps S
	group by S.recipe_id
	having count(distinct S.step) > 3
);

-- (d)
SELECT COUNT(*)
FROM recipes
WHERE EXISTS (
    SELECT 1
    FROM use
    JOIN ingredients ON use.ingredient_id = ingredients.id
    JOIN belong_to ON ingredients.id = belong_to.ingredient_id
    WHERE use.recipe_id = recipes.id AND belong_to.cuisine_id = recipes.belong_to
);

SELECT COUNT(DISTINCT recipes.id)
FROM recipes
JOIN use ON recipes.id = use.recipe_id
JOIN ingredients ON use.ingredient_id = ingredients.id
JOIN belong_to ON ingredients.id = belong_to.ingredient_id
WHERE belong_to.cuisine_id = recipes.belong_to;


-- (e)
SELECT recipes.name
FROM recipes
JOIN use ON recipes.id = use.recipe_id
GROUP BY recipes.id
HAVING COUNT(DISTINCT use.ingredient_id) = (
    SELECT MAX(num_ingredients)
    FROM (
        SELECT recipe_id, COUNT(DISTINCT ingredient_id) as num_ingredients
        FROM use
        GROUP BY recipe_id
    ) AS ingredient_counts
);

-- (f)
WITH spice_counts AS (
    SELECT cuisine_id, COUNT(*) as num_spices
    FROM ingredients
    JOIN belong_to ON ingredients.id = belong_to.ingredient_id
    WHERE ingredients.type = 'spice'
    GROUP BY cuisine_id
),
total_counts AS (
    SELECT cuisine_id, COUNT(*) as num_total
    FROM ingredients
    JOIN belong_to ON ingredients.id = belong_to.ingredient_id
    GROUP BY cuisine_id
),
ratios AS (
    SELECT total_counts.cuisine_id, (spice_counts.num_spices::float / total_counts.num_total::float) as spice_ratio
    FROM total_counts
    JOIN spice_counts ON total_counts.cuisine_id = spice_counts.cuisine_id
)
SELECT COUNT(*)
FROM ratios
WHERE spice_ratio = (
    SELECT MIN(spice_ratio)
    FROM ratios
);

-- (g)
SELECT COUNT(*)
FROM recipes
WHERE EXISTS (
    SELECT 1
    FROM use
    JOIN ingredients ON use.ingredient_id = ingredients.id
    WHERE use.recipe_id = recipes.id
    GROUP BY use.step
    HAVING COUNT(DISTINCT ingredients.type) = (
        SELECT COUNT(DISTINCT type)
        FROM ingredients
    )
);

-- (h)
drop view if exists indian_chefs;
create view indian_chefs as
select distinct C.id, C.name
from chefs C
     join recipes R on R.created_by = C.id
     join cuisines CU on CU.id = R.belong_to
where CU.name like '%Indian%';

select C.id, C.name, sum(quantity)
from indian_chefs C
     join recipes R on R.created_by = C.id
     join use U on U.recipe_id = R.id --18m
     join belong_to B on B.ingredient_id = U.ingredient_id
     join cuisines CU on CU.id = B.cuisine_id
where CU.name like '%Thai%'
group by C.id, C.name
order by sum(quantity) desc

-- 328	"Katie Lee"	41
-- 100	"Yutaka Ishinabe"	36
-- 140	"Raymond Oliver"	36
-- 39	"Caesar Cardini, inventor of Caesar salad (1924)"	33
-- 228	"Connie Achurra"	29
-- etc / 150 rows in total


