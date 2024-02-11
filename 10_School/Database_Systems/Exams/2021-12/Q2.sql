CREATE FUNCTION CheckCuisines() RETURNS TRIGGER
AS $$ BEGIN
    -- Check 1: Is the quantity OK?
    IF (NEW.quantity <= 0) THEN
        NEW.quantity = 1;
    END IF;
    -- Check 2: Is the ingredient in the correct cuisine?
    IF NOT EXISTS (
        SELECT *
        FROM recipes R
            JOIN belong_to B on R.belong_to = B.cuisine_id
        WHERE R.id = NEW.recipe_id
            AND B.ingredient_ID = NEW.ingredient_id) THEN
        RAISE EXCEPTION 'There is no common cuisine';
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER CheckCuisines
AFTER INSERT ON use
FOR EACH ROW EXECUTE PROCEDURE CheckCuisines();

INSERT INTO use (recipe_id, step, ingredient_id, quantity, unit) VALUES (1, 1, 33, -1, 'lb');
INSERT INTO use (recipe_id, step, ingredient_id, quantity, unit) VALUES (1, 1, 34, -1, 'lb');
INSERT INTO use (recipe_id, step, ingredient_id, quantity, unit) VALUES (1, 1, 34, 1, 'lb');