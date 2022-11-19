import React from "react";
import {Link} from 'react-router-dom'

const ProjectItem = ({project, delete_project, create_project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.title}</td>
            <td>{project.linkGitHub}</td>
            <td>{project.users}</td>
            <td><button onClick={()=>delete_project(project.id)}type='button'>Delete</button></td>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {

    return (
        <div>
        <table>
            <th>ID Project</th>
            <th>Name Project</th>
            <th>Link GitHub</th>
            <th>ID Users</th>
            {projects.map((project_) => <ProjectItem project={project_} delete_project={delete_project}/>)}
        </table>
        <br></br>
        <br></br>
        <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList;