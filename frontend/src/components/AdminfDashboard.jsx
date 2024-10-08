
import { useEffect } from 'react'
import React  from 'react'
import { useSelector } from "react-redux"
import { Navigate } from 'react-router-dom'
import { getAdminfUser,refreshAdminf } from '../action/auth'
import { useDispatch } from 'react-redux'
import Navigation from '../components/Navigation'
import NavBar from './NavDashboard/NavBar'
import PieDemandes from './public/charts/PieDemandes'
import PiePreInscription from './public/charts/PiePreInscriptions';

const AdminfDashboard = () => {
  const dispatch=useDispatch()
  useEffect(() => {
    // Check if there's a token in local storage
    const token = localStorage.getItem('token');
    if (token) {
      dispatch(refreshAdminf());

  }

    

    dispatch(getAdminfUser());

    
}, [dispatch]);
  const state = useSelector(state => state.auth);
  if (state.isLoading) {
    return <h3>Loading....</h3>;
} else if (!state.isAuthenticated || !state.isAdminf) {
    return <Navigate to="/login" />;
} else {
    
  return (
    
    <div style={{flexDirection:'row'}}>
      <NavBar/>
      <br/><br/>
      <center>
        <h1 style={{color:"#004B8B"}}>Simple Resume : </h1>
        <br/><br/>

      </center>
      <div style={{flexDirection:'column',position:'absolute',marginLeft:"28%",border:"1px solid #ccc",padding:"3%",height:"fit-content"}}>

          <PiePreInscription/>
          <h5>Resume : Pré-Inscriptions</h5>
</div>           
 <div style={{flexDirection:'column',position:'absolute',marginLeft:"60%",border:"1px solid #ccc",padding:"3%",height:"fit-content"}}>

          <PieDemandes/>

          <h5>Resume : Demandes Générales</h5>
</div>     
 <h2></h2>
            <h2></h2>
            <h2></h2>

    </div>
  )
}
}





export default AdminfDashboard