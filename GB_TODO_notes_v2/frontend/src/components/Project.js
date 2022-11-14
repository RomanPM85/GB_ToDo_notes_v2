import React from "react";

const ProjectItem = ({project, delete_project}) => {
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
        <table>
            <th>ID Project</th>
            <th>Name Project</th>
            <th>Link GitHub</th>
            <th>ID Users</th>
            {projects.map((project_) => <ProjectItem project={project_} delete_project={delete_project}/>)}
        </table>
    )
}

export default ProjectList;