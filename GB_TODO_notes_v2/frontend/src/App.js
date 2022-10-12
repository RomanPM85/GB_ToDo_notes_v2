import React from 'react';
import axios from "axios";
//import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import ProjectList from "./components/Project.js";
import MenuItem from "./components/Menu.js";
import FooterItem from "./components/Footer.js";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
        };
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
            this.setState({
                'projects': response.data
            })
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <MenuItem/>
                <UserList users={this.state.users}/>
                <ProjectList projects={this.state.projects}/>
                <FooterItem/>
            </div>
        );
    }
}

export default App;