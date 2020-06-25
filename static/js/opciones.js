const tareas = document.getElementById('tareas');
const tareasdos = document.getElementById('tareasdos');

const listaTareas = Sortable.create(tareas,{
    group: {
        name: "lista-tareas",
        pull: false,
        put: false
    },
    handle: ".btn",
    dataIdAttr: "data-identificador",
    dragClass: "drag",

    store: {
        set: function(sortable){
            const orden = sortable.toArray();
            orden.join('-');
            localStorage.setItem(sortable.options.group.name, orden.join('-'));  
        },

        get: function(sortable){
            const orden = localStorage.getItem(sortable.options.group.name);
            return orden ? orden.split('-') : [];
        }
    },

});


const listatareasdos = Sortable.create(tareasdos,{
    group: {
        name: "lista-tareasdos",
        pull: false,
        put: false
    },
    handle: ".btn",
    dataIdAttr: "data-identificadordos",

    store: {
        set: function(sortable){
            const ord = sortable.toArray();
            ord.join('-');
            localStorage.setItem(sortable.options.group.name, ord.join('-'));  
        },

        get: function(sortable){
            const ord = localStorage.getItem(sortable.options.group.name);
            return ord ? ord.split('-') : [];
        }
    },

});