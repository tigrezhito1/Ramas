import React from "react";


import { connect } from 'react-redux';




const Proveedores = ({proveedores,total_carteras}) =>{

      return (

      
        <div>


           
             <div className='row'>

                <div class='col-md-3'> <h3># Proveedor {proveedores.length} </h3></div>
                <div class='col-md-3'><h3>Industria</h3></div>
                <div class='col-md-3'><h3># Carteras {total_carteras}</h3></div>

            </div>

          

          <ul class="list-group">


                
               

             
            {proveedores.map(product=>
            
            <li class="list-group-item">
                
            <div className='row'>

                <div class='col-md-3'> {product.nombre}  </div>
                <div class='col-md-3'>
                            { 
                            product.industria ? product.industria.nombre : 'No tiene'
                            }
                </div>

                <div class='col-md-3'>
                           <a href={'/discador/carteras/' + product.id}>{product.contar_carteras}</a> 
                </div>



            </div>
            

            </li>



            )}
            

          </ul>


          </div>

          
       
      );


    }

const  mapStateToProps = state =>{


    console.log(state)

    return{
        proveedores:state.proveedores,
        deltas:state.deltas,
        total_carteras:state.total_carteras
    }

}









export default connect(mapStateToProps)(Proveedores);