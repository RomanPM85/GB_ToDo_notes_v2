import React from "react";

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

const ProjectList = ({projects}) => {

    return (
        <table>
            <th>
                ID Project
            </th>
            <th>
                Name Project
            </th>
            <th>
                Link GitHub
            </th>
            <th>
                ID Users
            </th>
            {projects.map((project_) => <ProjectItem project={project_}/>)}
        </table>
    )
}

export default ProjectList;