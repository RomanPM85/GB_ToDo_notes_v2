import React from "react";
import {useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.title}
            </td>
            <td>
                {project.linkGitHub}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectsUser = ({projects}) => {
    let {userId} = useParams()
    console.log(userId)
    let filter_projects = projects.filter((project)=> project.users.includes(parseInt(userId)))
    return (
        <table>
            <th>ID Project</th>
            <th>Name Project</th>
            <th>Link GitHub</th><th>ID Users</th>
            {filter_projects.map((project_) => <ProjectItem project={project_}/>)}
        </table>
    )
}

export default ProjectsUser;