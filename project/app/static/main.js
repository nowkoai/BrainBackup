const App = {
	data() {
	  return {
	    task: {title: ''},
	    tasks:['HTMLより'],
	  }
	  },
	compilerOptions: {
	    delimiters: ['[[', ']]'],
	},
	methods: {
		sendRequest(url, method, data){
			const csrftoken = Cookies.get('csrftoken');
			const myHeaders = new Headers({
			    'Content-Type': 'application/json',
			});
			if(method !== 'get'){
			    myHeaders.set('X-CSRFToken', csrftoken)
			};
	    
			fetch(url, {
			    method: method,
			    headers: myHeaders,
			    body: data,
			})
			.then((response) => {
			    return response.json();
			})
			.then((response) => {
			    if (method == 'get') {
				this.tasks = response;
			    };
			    if (method == 'post') {
				this.task.title = ''
				this.getTasks();
			    };
			    if (method == 'put') {
				this.getTasks();
			    };
			    if (method == 'put' || method == 'delete') {
				this.getTasks();
			    };
			})
			.catch(error => {
			    console.error('There has been a problem with your fetch operation:', error);
			});
		},
		getTasks(){
			this.sendRequest(URL, 'get');
		},
		createTask(){
			this.getTasks();
			this.sendRequest(URL, 'post',JSON.stringify(this.task));
		},
		updateTask(task){
			this.getTasks();
			this.sendRequest(URL, 'put',JSON.stringify(task));
		},
		deleteTask(task){
			this.getTasks();
			this.sendRequest(URL, 'delete',JSON.stringify(task));
		},
	created() {
	  	this.getTasks();
	},
      },
}
Vue.createApp(App).mount('#app')

alert('main.js')