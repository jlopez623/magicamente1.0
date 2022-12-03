//Guardar el elemento y el contexto
const mainCanvas = document.getElementById("main-canvas");
let context = mainCanvas.getContext("2d");
let rect = mainCanvas.getBoundingClientRect();

let initialX = 0;
let initialY = 0, dibujando = false, color='black', grosor=1;

function dibujar(x1, y1, x2, y2){
    
    context.beginPath();
    context.strokeStyle=color;
    context.lineWidth=grosor;
    context.moveTo(x1,y1);
    context.lineTo(x2,y2);
    context.stroke();
    context.closePath();


}


function defcolor(c){
    color = c;
}

function defgrosor(g){
    grosor = g;
}

mainCanvas.addEventListener('mousedown',function(e){
    initialX= e.clentX-rect.left;
    initialY= e.clentY-rect.top;
    dibujando = true;
    
});

mainCanvas.addEventListener('mousemove', function(e){

    if(dibujando===true){
        dibujar(initialX, initialY, e.clentX-rect.left, e.clentY-rect.top);

        initialX= e.clentX - rect.left
        initialY= e.clentY - rect.top

        
    }

})

mainCanvas.addEventListener('mouseup', function(e){
    if (dibujando===true){
        dibujar(initialX, initialY, e.clentX - rect.left, e.clentY - rect.top);
        initialX = 0;
        initialY = 0;
        dibujando = false;
    }
})




    
