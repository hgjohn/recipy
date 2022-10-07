//Returns an Array of Ingredients
const getIngredients = data => {
    const arr = [];
    /*Ingredients are stored in the database as objects named strIngredients
    with a number on the end. Eventually, strIngredient${i} returns a falsy value.*/

    //strIngredient is nested within the meal object, and 0th index array.

    for (let i = 1; data.meals[0][`strIngredient${i}`]; i++) {
        arr.push(data.meals[0][`strIngredient${i}`])
    }
    return arr;
}

const fetchMeal = mealName => {
    //Database returns data contained in key value pairs when given a s=recipe
    const api = `https://www.themealdb.com/api/json/v1/1/search.php?s=${mealName}`
    fetch(api)
    .then((response) => response.json())
    .then((response) => console.log(getIngredients(response)));
}

