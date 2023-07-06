$(document).ready(function () {


    if(navigator.geolocation){      
        navigator.geolocation.getCurrentPosition(ObtenerLocalizacion);
    }else{
        alert("No autoriza");
    }

    function ObtenerLocalizacion(position){
        console.log(position.coords.latitude+" "+position.coords.longitude);

        $.get("https://api.open-meteo.com/v1/forecast?latitude="+position.coords.latitude+"&longitude="+position.coords.longitude+"&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m", function(data){
            console.log(data);
     
        
           $("#temperatura").html(data["current_weather"]["temperature"]+" °C"); 
           $("#viento").html(data["current_weather"]["windspeed"]+" km/hr"); 
    
        
        });
     
    }

    $("#btnenviar2").click(function(e){
    
    
         if(validarformulario2()!= ""){
            swal("Error de Registro", validarformulario2(), "warning");
        }else{
            swal("Registrado correctamente", validarformulario2(), "success");
            /* swal("Datos enviados"); */
        }
   
        e.preventDefault();

    });


    function validarformulario2(){
        // nombre - apellido - fecha nac  - telefono - correo - rut -region - direccion- cod postal - contraseña - confirmar contraseña.
        var html=""; 
        
        
        var nombre =$("#txtnombre").val();
        var apellido =$("#txtapellidos").val();
        var fechnac =$("#txtFnac").val();
        var telefono =$("#txttelefono").val();
        var correo =$("#txtemail").val();
        var contrasena =$("#txtcontra").val();
        var confircontrasena =$("#txtconfirmacion").val();
        var region =$("#cbxCiudad").val();
        var direccion =$("#txtdireccion").val();
        var codpostal =$("#txtcodpostal").val();



       /* 

        
       
        var correo =$("#txtemail").val();
        var rut =$("#txtRut").val();
        var region =$("#").val();
        var direccion =$("#").val;
        var codpostal =$("#").val;
        
        var confircontrasena =$("#").val; */
        if(nombre=="")
        
        {
            html+="-Debe agregar un nombre \n";
        }

        if(apellido=="")
        {
            html+="-Debe agregar un apellido \n"
        }
        

        if(fechnac=="")
        
        {
            html+="-Debe agregar una fecha de nacimiento \n";
        }
        if(telefono=="")
        
        {
            html+="-Debe agregar un numero de telefono \n";
        }
        if(correo=="")
        
        {
            html+="-Debe agregar un correo electronico \n";
        }
        if(contrasena=="")
        
        {
            html+="-Debe agregar una contraseña \n";
        }
        if(confircontrasena=="")
        
        {
            html+="-Debe confirmar su contraseña \n";
        }

        if(($("#rbtnRUT")).is(":not(:checked)")  &&  ($("#rbtnPasaporte")).is(":not(:checked)")){
            html += "-Debe Seleccionar Tipo de Identificacion \n";
        }else{
            if(($("#rbtnRUT")).is(":checked")){
                if(validarRut($("#txtidentificador").val())==false){
                    html += "-Debe Ingresar un RUT Valido \n";
                }
            }
        }


        function validarRut(rutCompleto) {
            // Primero eliminamos cualquier caracter que no sea número o k/K
            rutCompleto = rutCompleto.replace("‐", "-");
        
            // Luego validamos que el formato del RUT sea válido
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
                return false;
        
            // Separamos el número del dígito verificador    
            var tmp = rutCompleto.split('-');
            // Calculamos el dígito verificador esperado
            var digv = tmp[1];
            var rut = tmp[0];
            if (digv == 'K') digv = 'k';
            // Comparamos el dígito verificador ingresado con el esperado
            return (dv(rut) == digv);
        }
        
        function dv(T) {
            var M = 0,
                S = 1;
            for (; T; T = Math.floor(T / 10))
                S = (S + T % 10 * (9 - M++ % 6)) % 11;
            return S ? S - 1 : 'k';
        }

        if(region==0)
        {
            html+="-Debe seleccionar una region \n";
        }

        if(direccion=="")
        
        {
            html+="-Debe indicar una direccion \n";
        }
        if(codpostal=="")
        
        {
            html+="-Debe indicar un codigo postal. \n";
        }



      return html;

 

  }





   




});