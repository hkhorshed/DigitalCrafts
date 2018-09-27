function apiData(response) {

    return {
        type: 'apiFetchData',
        apiMovieData: response
    }
}

export default apiData