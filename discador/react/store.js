import { createStore,applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

const cart = (state=[],action) => {

    if(action.type==='ADD_TO_CART'){
        return state.concat(action.product)
    }


    return state;


}

const proveedores = (state=[],action) => {

if(action.type==='PROVEEDORES'){
    return action.proveedores;
}
 return state;


 
}



const todoAgentes = (state=[],action) => {

    if(action.type==='TRAE_TODOS_AGENTES'){
        return action.todoAgentes;
    }
    return state;

}






const trae_carteras_proveedor = (state=[],action) => {

    if(action.type==='TRAE_CARTERAS_PROVEEDOR'){
        return action.trae_carteras_proveedor;
    }
     return state;
    
    
     
    }




const id_gestiones = (state=[],action) => {

    if(action.type==='TRAE_ID_GESTIONES'){

        console.log('INGRESE TRAE_ID_GESTIONES')

        return action.id_gestiones;
    }
        return state;
    
}



const resultados = (state=[],action) => {

    if(action.type==='TRAE_DATOS_RESULTADOS'){

        return action.resultados;
    }
        return state;
    
}

const subresultados = (state=[],action) => {

    if(action.type==='TRAE_DATOS_SUBRESULTADOS'){

        return action.subresultados;
    }
        return state;
    
}



const total_carteras = (state=[],action) => {

    if(action.type==='TOTAL_CONTADOR'){
        return action.total_carteras;
    }

    return state;
}




const gestiones = (state=[],action) => {

    if(action.type==='TRAE_GESTIONES'){
        return action.gestiones;
    }
    return state;
    
}



const score = (state=[],action) => {

    if(action.type==='TRAE_DATOS_SCORE'){
        return action.score;
    }
    return state;

}




const score_negocios = (state=[],action) => {

    if(action.type==='TRAE_DATOS_NEGOCIOS_SCORE'){
        return action.score;
    }
    return state;

}



const trae_cuentas = (state=[],action) => {


    if(action.type==='TRAE_CUENTITAS'){
        return action.trae_cuentas;
    }
    return state;

}


const carteras = (state=[],action) => {

    if(action.type==='TRAE_CARTERAS'){
        return action.carteras;
    }
    return state;

}

const traeAgentes = (state=[],action) => {

    if(action.type==='TRAE_AGENTES'){
        return action.traeAgentes;
    }
    return state;

}


const negocios = (state=[],action) => {

    if(action.type==='TRAE_NEGOCIOS'){
        return action.negocios;
    }

    return state

}

const detalle_cuentas = (state=[],action) => {

    if(action.type==='TRAE_DETALLE_CUENTAS'){
        return action.detalle_cuentas;
    } 

    return state;

}


const trae_telefonos = (state=[],action) => {

    if(action.type==='TRAE_TELEFONOS'){
        return action.trae_telefonos;
    } 

    return state;

}

const proveedor_cartera_negocio = (state=[],action) => {

    if(action.type==='TRAE_PROVEEDOR_CARTERA_NEGOCIO'){
        return action.proveedor_cartera_negocio;
    } 

    return state;

}


const logger = store => next => action => {
    console.log('dispatching', action)
    let result = next(action)
    console.log('next state', store.getState())
    return result
  }


export default createStore(combineReducers({todoAgentes,traeAgentes,proveedor_cartera_negocio,trae_telefonos,negocios,carteras,cart,proveedores,gestiones,total_carteras,trae_cuentas,score,trae_carteras_proveedor,id_gestiones,resultados,subresultados,detalle_cuentas}),applyMiddleware(logger,thunk));
