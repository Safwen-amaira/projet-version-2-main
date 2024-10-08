
import { useEffect } from 'react'
import React  from 'react'
import { useSelector } from "react-redux"
import { Navigate } from 'react-router-dom'
import { getAdminsUser ,refreshAdmins} from '../action/auth'
import { useDispatch } from 'react-redux'
import NavAdminS from '../components/NavDashboard/NavAdminS'
import NavBar from './NavDashboard/NavBar'
import PieDemandes from './public/charts/PieDemandes'
import PiePreInscription from './public/charts/PiePreInscriptions';

const AdminsDashboard = () => {
  const dispatch=useDispatch()
  useEffect(()=>{
    const token = localStorage.getItem('token');
    if (token) {
      dispatch(refreshAdmins());

  }

    dispatch(getAdminsUser())
      
  }, [dispatch])
  const state = useSelector(state => state.auth);
  if (state.isLoading) {
    return <h3>Loading....</h3>;
} else if (!state.isAuthenticated || !state.isAdmins) {
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



export default AdminsDashboard