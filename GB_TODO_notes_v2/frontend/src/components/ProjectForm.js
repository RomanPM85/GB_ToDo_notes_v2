import React from 'react'


class ProjectForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    title: '',
    linkGitHub: '',
    users: []
    }
  }

  handleChange(event) {
    this.setState({
    [event.target.name]: event.target.value
    })
  }

  handleUserChange(event) {
      if (!event.target.selectedOptions) {
          this.setState({
              'users': []
            })
            return;
      }
      let users = []
      for(let i = 0; i < event.target.selectedOptions.length;i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState(
            {'users':users}
        )
  }

  handleSubmit(event) {
    this.props.create_project(this.state.title, this.state.linkGitHub, this.state.users)
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={(event) => this.handleSubmit(event)}>
        <br></br>

        <label for="title">Проект
            <div>
              <input type="text" name="title" value={this.state.title}
              onChange={(event) => this.handleChange(event)}/>
            </div>
        </label>

        <label for="linkGitHub">GitHub
            <div>
              <input type="text" name="linkGitHub" value={this.state.linkGitHub}
               onChange={(event) => this.handleChange(event)}/>
            </div>
        </label>

        <br></br>
        <label for="users">Авторы
             <div>
                <select name="users" multiple
                    onChange={(event) => this.handleUserChange(event)}>
                    {this.props.users.map((item) => <option
                    value={item.id}>{item.last_name}</option>)}
                </select>
            </div>
        </label>
        <br></br>
        <input type="submit" value="Сохранить" />
      </form>
    );
  }
}

export default ProjectForm
