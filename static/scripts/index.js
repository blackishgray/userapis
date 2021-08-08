$(() => {

	var tableData = document.getElementById('table-data')
	
	// function to get the entire data from api
	const userslist = () => {

		// set the initial data in the table to empty
		tableData.innerHTML = ''


		let url = 'https://userapis.herokuapp.com/api/api/usersList';
		
		// fetch promise for rendering 
		// data from the api
		fetch(url)
		.then((response) => {
			return response.json()
		})
		.then(function(data){


			 var users = data 

			 for (let i in users){
			 	// dynamic html elements for every element
			 	// in the data received 
			 	var user = `

			  	<tr>
			  		<td>${users[i].first_name}</td>
			  		<td>${users[i].last_name}</td>
			  		<td>${users[i].email}</td>
			  		<td>${users[i].age}</td>
			  		<td>${users[i].dob}</td>
			  		<td>${users[i].mobile_no}</td>
			  	</tr>
			  `	
			  // updating the elements 
			  tableData.innerHTML += user

			 }

		})

	}

	userslist();


	// filtering data 
	$('#submitBtn').click((e) =>{

		let form = $('#filter-form')

		let csrftoken = $('input[name=csrfmiddlewaretoken]').val();
		let first_name = $('#first_name').val()
		let last_name = $('#last_name').val()
		let age = $('#age').val()
		let dob = $('#dob').val()

		let query = ''

		var url ;

		// if one input is given then 
		// filter through data using that input
		if (first_name){
			url = `https://userapis.herokuapp.com/api/userFilterFirstName/${first_name}`
		} else if (last_name) {
			url = `https://userapis.herokuapp.com/api/userFilterLastName/${last_name}`
		} else if (age){
			url = `https://userapis.herokuapp.com/api/userFilterAge/${age}`
		} else if (dob) {
			url = `https://userapis.herokuapp.com/api/userFilterDob/${dob}`
			
		}

		$.ajax({
			method:"GET",
			headers : {
				'Content-Type': 'application/json',
				'X-CSRFToken' : csrftoken,
			},
			url : url,
			success: (response) => {
			
				form.trigger('reset')
			
				tableData.innerHTML = ''

				console.log(response)

				var users = response

				console.log(users)

				 for (let i in users){
				 	var user = `
				  	<tr>
				  		<td>${users[i].first_name}</td>
				  		<td>${users[i].last_name}</td>
				  		<td>${users[i].email}</td>
				  		<td>${users[i].age}</td>
				  		<td>${users[i].dob}</td>
				  		<td>${users[i].mobile_no}</td>
				  	</tr>
				  `	
				  tableData.innerHTML += user
			}
		}

		})

	})

	$('#reset-btn').click( () => { 
		console.log('dj');
		userslist()
	})

	// function to create a new user 
	const submitUser = () => {
		// console.log('heloe');

		// url for create request
		let url = 'https://userapis.herokuapp.com/api/userCreate'

		let first_name = $('#form-first-name').val()
		let last_name = $('#form-last-name').val()
		let email = $('#form-email').val()
		let age = $('#form-age').val()
		let dob = $('#form-dob').val()
		let mobile_no = $('#form-mobile-no').val()

		let csrftoken = $('input[name=csrfmiddlewaretoken]').val();

		data = {first_name:first_name, last_name:last_name, email:email,
				age:age, dob:dob, mobile_no:mobile_no}

		// console.log(data)

		$.ajax({
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken' : csrftoken,
			},
			method:'POST',
			url : url,
			data : data,
			success:()=>{
				// console.log('Form Submitted')
				// call to userList function to update data table
				userslist()
			},
			fail: ()=>{
				console.log('Fail')
			}
		})
	}

	$('#submit-User').click(()=>{
		submitUser();

	})


})
