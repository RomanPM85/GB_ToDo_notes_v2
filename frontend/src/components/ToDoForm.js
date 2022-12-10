import React from 'react'


class ToDoForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    text: 'CrateToDo',
    status: 'active',
    project: '',
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
    this.props.create_todo(this.state.text, this.state.status, this.state.project, this.state.users)
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={(event) => this.handleSubmit(event)}>
        <br></br>

        <label for="text">Текст заметки
            <div>
              <input type="text" name="text" value={this.state.text}
              onChange={(event) => this.handleChange(event)}/>
            </div>
        </label>

        <label for="status">Статус
            <div>
              <input type="text" name="status" value={this.state.status}
               onChange={(event) => this.handleChange(event)}/>
            </div>
        </label>

        <br></br>

        <label for="project">Проект
            <div>
              <input type="text" name="project" value={this.state.project}
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

export default ToDoForm
