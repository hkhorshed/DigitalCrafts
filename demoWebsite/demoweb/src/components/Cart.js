import React from 'react';

import AddMovie from './AddMovie';



class Cart extends React.Component {
    constructor(props) {
        super(props);
        
    }

    componentWillMount(){
        fetch('http://www.omdbapi.com/?s=godfather&apikey=60a5989b')
        
        .then((response => response.json()))
        .then(response => this.props.onFetch(response))
       
    }



    render() { 

    var movies = []
    
    if (this.props.movieData.Search !== undefined){

        if (this.props.movieData.Search.length > 0) {
        movies = this.props.movieData.Search.map( movie => {
           return (
           <div> 
                <li> <b>{movie.Title}</b></li>
                <li>{movie.year} <br/> <img src={movie.Poster} alt="Movie Cover"/></li>
                <li>{movie.Title}</li>
           </div>   
           )
       })
       
        }}

        return (
            <div>
                <AddMovie AddMovie={this.props.onAddMovie} />
{movies}
                <table>
                    <thead>
                        <tr>
                            <th>Movie Name</th>
                            <th>Movie Cover Page</th>
                            <th>#</th>
                        </tr>
                    </thead>
                    <tbody>                    
                        {
                                this.props.movieList.map(movieData => {
                                return <tr key={movieData.movieName}>
                                    <td>{movieData.movieName}</td>
                                    <td><img src={movieData.moviePic} alt="moviePic"/></td>
                                    <button onClick={() => {
                                        this.props.onDeleteMovie(movieData)
                                    }}>Remove</button>
                                </tr>
                            })
                        }
                    </tbody>
                </table>
            </div>
        );
    }
}



export default Cart