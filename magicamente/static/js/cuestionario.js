


const lista1 = [
  "1 ¿Dedico tiempo para viajar?",
  "2 ¿Sé y tengo por escrito las metas que quiero lograr?",
  "3 ¿Hago actividad física regularmente? \n*La recomendación es mínimo 3 veces por semana.",
  "4 ¿Disfruto cada instante que la vida me da?",
  "5 ¿Dedico tiempo para leer? \n*La recomendación es un libro por mes.",
  "6 ¿me considero una persona sana?",
  "7 ¿Tengo ahorros para el futuro",
  "8 ¿Tengo fuente de ingresos adicionales?",
  "9 ¿Tengo mi peso ideal?",
  "10 ¿me considero un ser sociable?",
  "11 ¿Qué tantos momentos de diversión tengo?",
  "12 ¿Me gustan las reuniones familiares?",
  "13 ¿Disfruto las reuniones sociales?",
  "14 ¿Reviso mi estado de salud por lo menos una vez al año? \n*La recomendación es: exámenes de trigliceridos",
  "15 ¿Compro lo que realmente necesito?",
  "16 ¿Mis comidas son saludables y bien balanceadas? \n*La recomendación es comer 5 veces al día verduras",
  "17 ¿dedico tiempo para reflexionar sobre mis fortalezas y debilidades?",
  "18 ¿Comparto con mi familia tiempo de calidad?",
  "19 ¿cómo está mi carácter?",
  "20 ¿desempeño mi trabajo con excelencia?",
  "21 ¿Veo y/o escucho contenidos que considere aporten a mi conocimiento y edifiquen mi ser?",
  "22 ¿Promuevo la unidad familiar? ",
  "23 ¿cultivo buenos sentimientos? ",
  "24 ¿Presupuesto mis gastos mensuales?",
  "25 ¿Me considero una persona positiva? *La recomendación es hablar siempre en positivo",
  "26 ¿Tengo metas económicas claramente definidas?",
  "27 ¿Qué tan estable soy con mi trabajo?",
  "28 ¿estoy trabajamdo en lo que me gusta?",
  "29 ¿qué tanto me gusta mi cuerpo?",
  "30 ¿Medito habitualmente?",
  "31 ¿Cuido el planeta ahorrando agua y energía? \n*La recomendación es apagar las luces que no sean necesariasa y utilizar solo el agua necesaria.?",
  "32 ¿Qué tan conconsciente soy de mi respiración? \n*El aire oxigena el cerebro y te ayuda a descansar",
  "33 ¿Me cosidero una persona espiritual, quien busca cada día ser mejor?",
  "34 ¿Deposito la basura en la caneca correspondiente siempre?\nOrgánico, Ordinario, Reciclable",
  "35 ¿Tengo alguna herramienta que me ayude a enfocar mis sueños?\nEj. Mapa de los sueños.",
  "36 ¿Llevo registro por escrito de todos mis ingresos y egresos de cada mes?",
  "37 ¿Tengo interés permanente en aprender y sé lo que quiero aprender?",
  "38 ¿Qué tanto sé administrarmi dinero?",
  "39 ¿Aprovecho mis talentos?",
  "40 ¿Qué tan disciplinado soy?",
  "41 ¿Soy feliz?",
  "42 ¿Tengo buenos amigos?\n Personas que me alludan a ser mejor",
  "43 ¿Siento pasión por lo que hago en la actualidad?",
  "44 ¿Consigo materialmente lo que me propongo?",
  "45 ¿Comparto frecuentemente con mis amigos?",
  "46 ¿Aprovecho las oportunidades que veo para avanzar en mi campo laboral?",
  "47 ¿Con qué frecuencia juego con mi niño interior? (Hacer, siendo adulto, lo que me gustaba hacer cuando pequeño).",
  "48 ¿Considero que cómo lo necesario y no me excedo?",
  "49 ¿Cómo se encuentra mi autoestima?\n(Me amo, cultivo buenos sentimientos, buenos pensamientos y buenas acciones, dedico tiempo para mi).",
  "50 ¿Me gusta mi personalidad?",
  "51 ¿Tengo clara la misión con mi trabajo?",
  "52 ¿Hago con frecuencia lo que me divierte?",
  "53 ¿Me siento orgulloso de mi familia?",
  "54 ¿Qué tanto confio en las personas que llegan a mi vida?",
  "55 ¿Pienso que la vida es divertida?",
  "56 ¿Me considero una persona agradecida?",
  "57 ¿Qué tanto sirvo a los demás?",
  "58 ¿Qué tanto sonrío?",
  "59 ¿Cuido mis palabras al hablar?",
  "60 ¿Me perdono y perdono con facilidad?",
  "61 ¿Me siento pleno con mi pareja \n Si no tengo pareja como me siento sin tenerla?",
  "62 ¿Me gusta escuchar música y lo hago?",
  "63 ¿Qué tanto apoyo a mi familia en los momentos de dificultad?",
  "64 ¿Siento que mi familia me ha infundado principios y valores?",
  "65 ¿Qué tanto expreso mis sentimientos?",
  "66 ¿Tengo claras mis metas laborales?",
  "67 ¿Qué tanto está presente el amor en mi vida en todo ámbito?",
  "68 ¿Me considero divertido?",
  "69 ¿Mantengo una comunicación constante y directa con mis familiares?",
  "70 ¿Promuevo el ahorro en mi familia?",
  "71 ¿Siento que con mi trabajo estoy aportando para una sociedad mejo?",
  "72 ¿Qué tanto sentido de pertenencia tengo por el lugar donde trabajo?",
  "73 ¿Qué tan estable soy con mis amistades?",
  "74 ¿Respeto y cuido los animales?",
  "75 ¿Me considero buen amigo?",
  "76 ¿Qué tanto disfruto estar en contacto con la naturaleza?",
  "77 ¿He sembrado árboles o plantas?",
  "78 ¿qué tan cuidadoso soy con mis pertenencias?",
  "79 ¿Qué tanto aporto en no arrojar basuras? \n(En ríos, maresm quebradas, ciudad, bosques y en todo lugar)",
  "80 ¿Qué tan agradecido soy con todas las provisiones de la madre tierra?",
];

function listaParticion(a, b) {
  const preguntas = document.getElementById("preguntascont");
  let lista = lista1.slice(a, b);
  if (b <= 80) {
    for (let e of lista) {
        div = document.createElement('div');
        div.setAttribute("class", "question");

        label = document.createElement('label');
        label.innerText = e;
        p = document.createElement('p');

        input = document.createElement('input');
        input.setAttribute("type", "range");
        input.setAttribute("name", "pregunta" + lista.indexOf(e));
        input.setAttribute("id", "id" + lista.indexOf(e));
        input.setAttribute("min", "10");
        input.setAttribute("max", "100");
        input.setAttribute("step", "10");
        input.setAttribute("value", "10");
        input.setAttribute("onchange", "document.getElementById( " + "'out" + lista.indexOf(e) + "'" + ").value = value");

        input.setAttribute("list", "tickmarks");

        output = document.createElement('output');
        output.setAttribute("id", "out" + lista.indexOf(e));
        output.setAttribute("for", `pregunta${lista.indexOf(e)}`);



        output.innerText = '10';
        p.appendChild(input);
        p.appendChild(output);
        label.appendChild(p);
        div.appendChild(label);

        preguntas.appendChild(div);
    }
  }
  const btnSiguiente = document.createElement("input");
  btnSiguiente.setAttribute("class", "botonGrafico");
  btnSiguiente.setAttribute("type", "submit");
  btnSiguiente.setAttribute("value", "Generar");
  btnSiguiente.setAttribute("name", "siguiente");
  const span = document.createElement("span");

  //span.setAttribute("class", "spanb");

  preguntas.appendChild(span);
  span.appendChild(btnSiguiente);

  return preguntas;
}

//let btnSiguiente = document.querySelector(".boton");

var inicio = 0;
var fin = 80;


const form = document.getElementById("preguntascont");

form.addEventListener("submit", function (event) {
  event.preventDefault();
  let dataNode = document.querySelectorAll("output");
  listav = [];

  for (var value of dataNode.values()) {
    let d = value.innerText;
    let num = parseInt(d);
    listav.push(num);
  }

  console.log("submit", listav);
  //document.getElementById('preguntascont').reset();
  inicio = inicio + 20;
  fin = fin + 20;
  return listav, clear(), grafGen();
});

function clear() {
  console.log("limpiando");
  form2 = document.getElementById("preguntascont");
  form2.remove();
}

function grafGen() {
  var listapruebas = listav;
  var marksCanvas = document.getElementById("chart");

  function obtenerValores() {
    var dataUser = [];
    //espiritual suma 4/17/30/33/39/49/56/60
    var espiritual =
      listapruebas[3] +
      listapruebas[16] +
      listapruebas[29] +
      listapruebas[32] +
      listapruebas[38] +
      listapruebas[48] +
      listapruebas[55] +
      listapruebas[59];
    dataUser.push(espiritual);

    //suma3+6+9+14+16+29+32+48
    var fisica =
      listapruebas[2] +
      listapruebas[5] +
      listapruebas[8] +
      listapruebas[13] +
      listapruebas[15] +
      listapruebas[28] +
      listapruebas[31] +
      listapruebas[47];
    dataUser.push(fisica);

    //suma 2+5+19+21+25+35+37+40
    var mental =
      listapruebas[1] +
      listapruebas[4] +
      listapruebas[18] +
      listapruebas[20] +
      listapruebas[24] +
      listapruebas[34] +
      listapruebas[36] +
      listapruebas[39];
    dataUser.push(mental);

    //suma: 23+41+43+50+59+61+65+67
    var emocional =
      listapruebas[22] +
      listapruebas[40] +
      listapruebas[42] +
      listapruebas[49] +
      listapruebas[58] +
      listapruebas[60] +
      listapruebas[64] +
      listapruebas[66];
    dataUser.push(emocional);

    //suma: 1+11+47+52+55+58+62+68
    var ludica =
      listapruebas[0] +
      listapruebas[10] +
      listapruebas[46] +
      listapruebas[51] +
      listapruebas[54] +
      listapruebas[57] +
      listapruebas[61] +
      listapruebas[67];
    dataUser.push(ludica);

    //suma 12+18+22+53+63+64+69+70
    var familiar =
      listapruebas[11] +
      listapruebas[17] +
      listapruebas[21] +
      listapruebas[52] +
      listapruebas[62] +
      listapruebas[63] +
      listapruebas[68] +
      listapruebas[69];
    dataUser.push(familiar);

    //suma 10+13+42+45+54+57+73+75
    var social =
      listapruebas[9] +
      listapruebas[12] +
      listapruebas[41] +
      listapruebas[44] +
      listapruebas[53] +
      listapruebas[59] +
      listapruebas[72] +
      listapruebas[74];
    dataUser.push(social);

    //suma 7+8+15+24+26+36+38+44
    var economica =
      listapruebas[6] +
      listapruebas[7] +
      listapruebas[14] +
      listapruebas[23] +
      listapruebas[25] +
      listapruebas[35] +
      listapruebas[37] +
      listapruebas[43];
    dataUser.push(economica);

    //suma 31+34+74++76+77+78+79+80
    var ecologica =
      listapruebas[30] +
      listapruebas[33] +
      listapruebas[73] +
      listapruebas[75] +
      listapruebas[76] +
      listapruebas[77] +
      listapruebas[78] +
      listapruebas[79];
    dataUser.push(ecologica);

    //suma 20+27+28+46+51+66+71+72
    var laboral =
      listapruebas[19] +
      listapruebas[26] +
      listapruebas[27] +
      listapruebas[45] +
      listapruebas[50] +
      listapruebas[65] +
      listapruebas[70] +
      listapruebas[71];
    dataUser.push(laboral);

    return dataUser;
  }
  var dataUser = obtenerValores();

  var marksData = {
    labels: [
      "Espritual",
      "Física",
      "Mental",
      "Emocional",
      "Lúdica",
      "Familiar",
      "Social",
      "Económica",
      "Ecológica",
      "Laboral",
    ],
    datasets: [
      {
        label: "Tu resultado",
        backgroundColor: "rgba(0,150,80,0.5)",
        data: dataUser,
      },
      {
        label: "Recomendado",
        backgroundColor: "rgba(255,0,0,0.2)",
        data: [800, 800, 800, 800, 800, 800, 800, 800, 800, 800],
      },
    ],
  };

  var chart = new Chart(marksCanvas, {
    type: "radar",
    data: marksData,
  });
}
