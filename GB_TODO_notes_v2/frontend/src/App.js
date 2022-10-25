import React from 'react';
import axios from "axios";
//import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import ProjectList from "./components/Project.js";
import ProjectsUser from "./components/ProjectUser.js";
import ToDOList from "./components/ToDo.js";
import Navbar from "./components/Menu.js";
import FooterItem from "./components/Footer.js";
import NotFound404 from "./components/NotFound404";
import LoginForm from './components/Auth.js';
import {BrowserRouter,
    Route,
    Routes,
    Link,
    Navigate
    } from "react-router-dom";
import Cookies from 'universal-cookie';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
//            auth: {username: '', is_login: false}
            'token': ''
        };
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
        this.setState({'users':[]},()=> this.load_data())
        this.setState({'projects':[]},()=> this.load_data())
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
            const users = response.data
            this.setState({
                'users': users
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
                this.setState({projects: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({books:[]})
            })

        axios.get('http://127.0.0.1:8000/api/todos/', {headers}).then(response => {
            this.setState({
                'todos': response.data
            })
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }


    render() {
        return (
            <div className="App">
                <Navbar/>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Номе</Link></li>
                        <li><Link to='/users'>UserList</Link></li>
                        <li><Link to='/projects'>ProjectList</Link></li>
                        <li><Link to='/todos'>ToDOList</Link></li>
                        <li>
                            {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
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
                        <Route exact path='/login' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>} />
                        }
                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
                <FooterItem/>
            </div>
        );
    }
}

export default App;