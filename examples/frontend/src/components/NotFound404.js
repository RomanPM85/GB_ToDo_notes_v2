import {useLocation} from "react-router-dom";
import React from "react";

const NotFound404 = () => {
    let {pathname} = useLocation()
    return(
        <div>
            <h1> Page not found ( {pathname} ) Ошибка 404 </h1>
        </div>
    )
}
export default NotFound404;
