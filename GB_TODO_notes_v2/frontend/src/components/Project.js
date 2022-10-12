import React from "react";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.title}
            </td>
            <td>
                {project.linkGitHub}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {

    return (
        <table>
            <th>
                Name Project
            </th>
            <th>
                Link GitHub
            </th>
            {projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default ProjectList;