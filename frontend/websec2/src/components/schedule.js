import React from 'react';
import axios from 'axios';
import classNames from 'classnames';
import 'bootstrap/dist/css/bootstrap.min.css';

class Schedule extends React.Component{
    static defaultProps;
    async getData() {
        // let table_rows = [];
        let apiUrl = `http://localhost:5000/api/get_week_schedule?week=${this.state.current_week}`;
        if (this.state.staffId != null)
        {
            apiUrl += `&staffId=${this.state.staffId}`;
        }
        else if (this.state.groupId != null)
        {
            apiUrl += `&groupId=${this.state.groupId}`;
        }
        const res = await axios(apiUrl);
        console.log(res);
        return await res.data; // (Or whatever)
    }
    async getCurrentWeek() {
        const apiUrl = `http://localhost:5000/api/get_current_week`;
        const res = await axios(apiUrl);
        console.log(res);
        return await res.data.current_week; // (Or whatever)
    }
    prevWeek() {
        
        
        (async () => {
        try {
            await this.setState({current_week: this.state.current_week-1});
            this.setState({data: null});
            this.setState({data: await this.getData()});
        } catch (e) {

        }
        })();
        return;
    }
    nextWeek()
    {
        (async () => {
            try {
                await this.setState({current_week: Number(this.state.current_week)+1});
                this.setState({data: null});
                this.setState({data: await this.getData()});
            } catch (e) {
    
            }
            })();
        return;
    }
    constructor(props) {
        super(props);
        console.log(props);
        this.state = {data: null, current_week: null, staffId: null};
        this.prevWeek = this.prevWeek.bind(this);
        this.nextWeek = this.nextWeek.bind(this);
    }
    static getDerivedStateFromProps(props, state)
    {
        if (props.staffId !== state.staffId || props.groupId !== state.groupId)
        {
            return {
                staffId: props.staffId,
                groupId: props.groupId,
            };
        }
        return null;
    }
    componentDidMount() {
        if (!this.state.current_week || (this.state.staffId !== this.props.staffId)) {
            (async () => {
                try {
                    await this.setState({current_week: await this.getCurrentWeek()});
                    // console.log(`current week: ${this.state.current_week}`);
                    if (this.state.current_week)
                        {
                        try {
                            this.setState({data: await this.getData()});
                        } catch (e) {
                            //...handle the error...
                        }
                    }
                } catch (e) {
                    //...handle the error...
                }
            })();
        }
    }
    componentWillReceiveProps(nextProps) {
        if (this.props !== nextProps)
        {
            (async () => {
                try {
                    await this.setState({current_week: await this.getCurrentWeek()});
                    // console.log(`current week: ${this.state.current_week}`);
                    if (this.state.current_week)
                        {
                        try {
                            this.setState({data: await this.getData()});
                        } catch (e) {
                            //...handle the error...
                        }
                    }
                } catch (e) {
                    //...handle the error...
                }
            })();
        }
    }

    render() {
        console.log(this.state);
        console.log(this.props);
        console.log(this.state.data? "null" : "hi");
        return (
            <div  class="schedule">

                {(this.state.data === undefined || this.state.data === null || this.state.data.constructor !== Array) ? <em>Загрузка...</em> : 
                <div >

                    {(this.state.current_week == null) ?  <em>Определение недели..</em> : 
                        <div class="test_week_div">
                            <button class="btn btn-info" onClick={this.prevWeek}>Предыдущая неделя</button>
                            <span class="current_week">{this.state.current_week} неделя</span>
                            <button class="btn btn-info" onClick={this.nextWeek}>Следующая неделя</button>
                        </div>
                        }
                    <table >
                        <tbody>
                      {
                        this.state.data.map((element, row_index) =>
                        <tr key={row_index} className={`${row_index === 0? "schedule_head": ""}`}>{
                          element.row_data.map((elem_td) =>
                          <td class="schedule_item">
                              {elem_td.text}  
                          </td>
                          )
                          }</tr>
                        )
                        
                      }
                      </tbody>
                    </table>
                    </div>
                    }
            </div>
        );
    }
}

export default Schedule;