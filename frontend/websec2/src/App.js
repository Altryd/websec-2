import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, {useEffect, useState} from 'react';
import Schedule from './components/schedule';
import SearchStaff from './components/searchStaff';
import SearchGroup from './components/searchGroup';


class App extends React.Component{
  static defaultProps;
  constructor(props) {
      super(props);
      console.log(document.cookie);
      let isStudentCookie = this.getCookieByName("isStudent");
      let groupIdCookie = this.getCookieByName("groupId");
      let staffIdCookie = this.getCookieByName("staffId");
      console.log(isStudentCookie, groupIdCookie, staffIdCookie);
      if (isStudentCookie != undefined && (groupIdCookie != undefined || staffIdCookie != undefined))
      {
        console.log("setting by cookie");
        isStudentCookie = (isStudentCookie == "true");
        if (groupIdCookie == null) groupIdCookie = null;
        else staffIdCookie = null;
        this.state = {isStudent: isStudentCookie, staffId: staffIdCookie, groupId: groupIdCookie};  
      }
      else
      {
        this.state = {isStudent: true, staffId: null, groupId: null};
      }
      this.radioButtonChanged = this.radioButtonChanged.bind(this);
      this.staffIdChanged = this.staffIdChanged.bind(this);
      this.groupIdChanged = this.groupIdChanged.bind(this);
  }
  getCookieByName(name)
  {
    return document.cookie.split('; ').filter(row => row.startsWith(`${name}=`)).map(c=>c.split('=')[1])[0];
  }
  radioButtonChanged()
  {
    // this.setState({isStudent: !this.state.isStudent, staffId: null, groupId: null});
    this.setState({isStudent: !this.state.isStudent});
    // console.log(this.state);
  }
  setCookie(staffId, groupId)
  {
    let studentCookie = true;
    if (staffId != null) 
    { 
      studentCookie = false;
      
      document.cookie = `staffId=${staffId}; SameSite=None; Secure`;  
      document.cookie = `groupId=${groupId}; Max-Age=0; SameSite=None; Secure`;
    }
    else
    {
      document.cookie = `staffId=${staffId}; Max-Age=0; SameSite=None; Secure`;
      document.cookie = `groupId=${groupId}; SameSite=None; Secure`;
    }
    document.cookie = `isStudent=${studentCookie}; SameSite=None; Secure`;
    
  }
  staffIdChanged(staffId) {
    this.setState({staffId: staffId});
    this.setState({groupId: null});
    this.setCookie(staffId, null);
  }
  groupIdChanged(groupId) {
    this.setState({groupId: groupId});
    this.setState({staffId: null});
    this.setCookie(null, groupId);
  }
  render()
  {
    let schedule_item = null;
    console.log('app state:');
    console.log(this.state);
    if (this.state.staffId != null) schedule_item = <Schedule staffId={this.state.staffId} key={this.state.staffId}/>;
    else if (this.state.groupId != null) schedule_item = <Schedule groupId={this.state.groupId} key={this.state.groupId}/>;
    else schedule_item = <Schedule/>;
    return (
      <div className="App">
        <div class="input-group-text">
        <input type="radio" name="choice" id="student" defaultChecked={this.state.isStudent} onChange={this.radioButtonChanged}>
          </input><label for="student">Студент</label>
        { (this.state.isStudent)? <SearchGroup groupCallback={this.groupIdChanged}/> : ""}
        </div>

        <div class="input-group-text">
        <input type="radio" name="choice" id="staff" defaultChecked={!this.state.isStudent} onChange={this.radioButtonChanged}>
          </input><label for="staff">Преподаватель</label>
        { !(this.state.isStudent)? <SearchStaff staffCallback={this.staffIdChanged}/> : ""}
        </div>
          {schedule_item}
          
          
      </div>
    );
  }

}
/*
function App() {
  return (
    <div className="App">
        <Schedule/>
        <SearchStaff/>
        <SearchGroup/>
    </div>
  );
}/*
/*
function get_staff()
{
  let staff_fio = "Алексей"
  axios.get(`http://localhost:5000/api/search_staff?fio=${staff_fio}`)
  .then((data) => {
    console.log("good");
    console.log(data);
  })
  .catch((error) => {
    console.log(error);
    console.log("error happened");
  })
}
*/
function get_week_schedule()
{
  let staff_fio = "Алексей"
  axios.get(`http://localhost:5000/api/get_week_schedule?fio=${staff_fio}`)
  .then((data) => {
    console.log("good");
    console.log(data);
    /*
    let initial_list = data.data;
    console.log(initial_list);
    let rows = [];
    let get_table = document.getElementById("test");
    for (let i = 0; i<initial_list.length; i++){
      let table_row = [];
      for (let j=0; j < initial_list[i].length; j++)
      {
        table_row.push(<td>{initial_list[i][j].text}</td>);
      }
      console.log(table_row);
      var table_row_element = document.createElement("tr", { className: "contexCon" }, table_row);
      get_table.appendChild(table_row_element);
      rows.push(<tr>{table_row}</tr>);
      // let get_table = document.getElementById("test");
      // test.appendChild(rows);
      //rows.push(<p>{data[i].name + ", " + data[i].age + " years old"}</p>)
    }
    console.log(rows); */
  })
  .catch((error) => {
    console.log(error);
    console.log("error happened");
  })
}

export default App;
