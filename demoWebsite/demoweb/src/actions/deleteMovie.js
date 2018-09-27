function deleteMovie(item) {

    return {
        type: "deleteMovie",
        movieData: {
            movieName: item.movieName,
            moviePic: item.moviePic
        }
    }
}

export default deleteMovie