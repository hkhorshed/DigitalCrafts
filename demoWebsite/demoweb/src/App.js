import {connect} from 'react-redux';
import Cart from './components/Cart';
import addMovie from './actions/addMovie';
import deleteMovie from './actions/deleteMovie';
import apiData from './actions/apiData';


function mapStateToProps(state){
  return{
    movieList: state.movieList,
    movieData: state.apiInfo
  }
}
function mapDispatchToProps(dispatch) {
  
  return {
    onAddMovie: (movieData) => dispatch(addMovie(movieData)),
    onDeleteMovie: (movieData) => dispatch(deleteMovie(movieData)),
    onFetch: (response) => dispatch(apiData(response))
  }
}


var connectedComponent = connect(
  mapStateToProps,
  mapDispatchToProps
)(Cart);

export default connectedComponent