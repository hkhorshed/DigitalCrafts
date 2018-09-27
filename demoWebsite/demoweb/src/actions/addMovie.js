

function addMovie(item) {
    
    return {
        type: "addMovie",
        movieData: {
            movieName: item.movieName,
            moviePic: item.moviePic
        }
    }
}

export default addMovie;