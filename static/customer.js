
$(document).ready(function () {
    $.getJSON('/api/customerlist', function (data) {
      var htm = `<table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Birth</th>
          <th scope="col">Contact Details</th>
          <th scope="col">Address</th>
          <th scope="col">Organisation Name</th>
          <th scope="col">Make Call</th>
          <th scope="col">Picture</th>
          <th scope="col">Follow Up</th>
          <th scope="col">Modification</th>
  
        </tr>
      </thead>
      <tbody>`
  
      data.map((item) => {
        htm += `<tr>
  <th th scope = "row" > ${item.id}</th> 
  <td>${item.firstname} ${item.lastname}</td>       
  <td>${item.dob}</td>       
  <td>${item.emailid} <br>${item.mobileno}<br>${item.alternateno}</td>       
  <td>${item.address} <br>${item.cityname}<br>${item.statename}</td>       
  <td>${item.organisationname} </td>           
  <td><a href="tel:${item.mobileno}"><img src="/static/calllogo.png" width="40" ></a></td>
  <td><a href='/api/display_customer_picture?customerid=${item.id}&customername=${item.firstname} ${item.lastname}&picture=${item.photograph}'><img src="/${item.photograph}" width="50" ></a></td>
  <td><a href='/api/callcustomerbyid?customerid=${item.id}'>Fill Details</a></td>
  <td><a href='/api/customerbyid?customerid=${item.id}'>Update/Delete</a></td>`
 
  
      })
  
      htm += `</tbody ></table > `
      $('#CustomerData').html(htm)
  
    })
  })