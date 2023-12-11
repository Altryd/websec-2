import React from 'react';
import axios from 'axios';

class SearchStaff extends React.Component {
    state = {
      query: "",
      data: [],
      filteredData: [],
      staffId: null,
    };
    handleInputChange = event => {
      const query = event.target.value;
      this.setState(prevState => {
        let filteredData = prevState.data.filter(element => {
            //console.log(element);
            /*if (element.name == null)
            {
                return element.name;
            }*/
          return element.fio.toLowerCase().includes(query.toLowerCase());
        });
        //console.log(filteredData);
       // console.log(filteredData);
        if (filteredData.length > 10) {filteredData = filteredData.slice(0, 10)};
        return {
          query,
          filteredData
        };
      });
    };
    handleClick(id) {
        //console.log(`staff id: ${id}`);
        this.setState({staffId: id});
        //console.log(this.state.staffId);
        this.props.staffCallback(id);
    }
    constructor(props) {
        super(props);
        // console.log(props);
        this.state = {query: "", data: null, filteredData: [], staffId: null};
        this.handleClick = this.handleClick.bind(this);
    }
    getData = () => {
        console.log(this.props);
        let URL = `http://localhost:5000/api/search_staff?fio=${this.state.query}`;
       // console.log(URL);
        // let URL = `http://localhost:5000/api/search_staff?fio=${this.state.query}`;
        axios.get(URL)
        .then(response => response.data)
        .then(data => {
          const { query } = this.state;
          // console.log(data);
          const filteredData = data.filter(element => {
            // console.log(element);
            return element.fio.toLowerCase().includes(query.toLowerCase());
          });
          this.setState({
            data,
            filteredData
          });
        });
    };
    componentDidMount() {
        if (!this.state.data)
        {
            this.getData();
        }
    }
    /*
    componentDidUpdate( prevState ) {
         if (prevState.staffId !== this.state.staffId ){
            console.log("onvaluechange");
            console.log(this.props);
            if (this.props.onValueChange != null) this.props.onValueChange(this.state.staffId);
        }
    } */
    render() {
      return (
        <div className="searchForm">
          <form>
            <input
              placeholder="Введите ФИО"
              value={this.state.query}
              onChange={this.handleInputChange}
            />
          </form>
          <div class="searchResults">{(this.state.query === "") ? "" : 
            this.state.filteredData.map(elem => <button className={"btn searchElement " +  (this.state.staffId == elem.id ? "btn-info" : "btn-outline-info")}
                id={elem.id} key={elem.id} onClick={() => {this.handleClick(elem.id)}}>{elem.fio}</button>)}
            </div>
        </div>
      );
    }
  }

  
export default SearchStaff;