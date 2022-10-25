import React from 'react'


class LoginForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {login: '', password: ''}
    }

    handleChange(event)
    {
        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
    }
    handleSubmit(event) {
      this.props.get_token(this.state.login, this.state.password)
      event.preventDefault()
    }

    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
                <label for="login">login</label>
                <input type="text" name="login" placeholder="Login" value={this.state.login} onChange={(event)=>this.handleChange(event)} />
            </div>
            <div className="form-group">
                <label for="password">password</label>
                <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event)=>this.handleChange(event)} />
            </div>
            <input type="submit" className="btn btn-primary" value="Login" />
        </form>
      );
    }
  }
export default LoginForm;
