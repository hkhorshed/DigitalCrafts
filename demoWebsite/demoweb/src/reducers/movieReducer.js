// reducer

// API Key
// http://www.omdbapi.com/?i=insertSelectedimdbIDhere&apikey=60a5989b

function movieReducer(state , action) {
        if (state === undefined) {
            console.log("This is the initial sate")
            return {
                movieList: [],
                apiInfo: []

        }
    }
        switch(action.type) {
            case "addMovie":
            return {
                ...state,
                movieList: state.movieList.concat( {
                    movieName: action.movieData.movieName,
                    moviePic: action.movieData.moviePic
                })
            }

            case "deleteMovie":

                const updatedMovieList = state.movieList.filter( movie => 
                    {
                        return movie.movieName !== action.movieData.movieName
                    })
                return {
                    ...state,
                    movieList: updatedMovieList
                }
            case "apiFetchData":
            {
                return {
                    ...state,
                    apiInfo: action.apiMovieData
                }
            }
            default:
                return (state)
        }
    }


export default movieReducer;