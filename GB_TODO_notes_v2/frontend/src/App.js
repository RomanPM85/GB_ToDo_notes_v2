import React from 'react';
import axios from "axios";
//import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import ProjectList from "./components/Project.js";
import ProjectsUser from "./components/ProjectUser.js";
import ToDOList from "./components/ToDo.js";
import MenuItem from "./components/Menu.js";
import FooterItem from "./components/Footer.js";
import NotFound404 from "./components/NotFound404";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
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

        axios.get('http://127.0.0.1:8000/api/todos/').then(response => {
            this.setState({
                'todos': response.data
            })
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <MenuItem/>
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/'>Номе</Link>
                        </li>
                        <li>
                            <Link to='/users'>UserList</Link>
                        </li>
                        <li>
                            <Link to='/projects'>ProjectList</Link>
                        </li>
                        <li>
                            <Link to='/todos'>ToDOList</Link>
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users'/>}/>
                        <Route path ='/users'>
                            <Route index element={<UserList users={this.state.users}/>}/>
                            <Route path=':userId' element={<ProjectsUser projects={this.state.projects}/>}/>
                        </Route>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todos' element={<ToDOList todos={this.state.todos}/>}/>
                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
                <FooterItem/>
            </div>
        );
    }
}

export default App;