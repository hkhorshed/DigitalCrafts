
// This index.js is the action page which contains all the actions required for the movie page.
// If there were more actions with different levels or categories then more pages would be required.


// Action to add a movie on the webpage
export const addMovie = movieData => ({
    type: 'addMovie',
    movieData: movieData,
})




// Action to delete a movie on the webpage
export const deleteMovie = movieData => ({
    type: "deleteMovie",
    movieData: movieData
})



// Action to fetch all the data from the OMDb API.
export const apiData = movieData => ({
    type: apiFetchData,
    movieData: movieData
})