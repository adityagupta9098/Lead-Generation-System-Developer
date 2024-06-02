// $(document).ready(function () {
//   $.getJSON("/api/callsearch", function (data) {
//     function table(data) {
//       var htm = `<table class="table table-hover">
//     <thead>
//       <tr>
//         <th scope="col">S.No.</th>
//         <th scope="col">Name</th>
//         <th scope="col">caller</th>
//         <th scope="col">Date</th>
//         <th scope="col">Phonestatus</th>
//         <th scope="col">Conversation</th>
//         <th scope="col">leadstatus</th>
//         <th scope="col">Mobileno</th>
//       </tr>
//     </thead>
//     <tbody>`;

//       data.map((item) => {
//         htm += `<tr>
//         <th scope="row">${item.id}</th>
//         <td>${item.customername}</td>
//         <td>${item.callerid}  ${item.status}<br>${item.callername}</td>
//         <td>${item.currentdate}</td>
//         <td>${item.phonestatus}</td>
//         <td>${item.conversation}</td>
//         <td>${item.leadstatus}</td>
//         <td>${item.mobileno}</td>
//         `;
//       });

//       htm += `</tbody> </table>`;

//       $("#calldetailsData").html(htm);
//     }
//   });
// });
