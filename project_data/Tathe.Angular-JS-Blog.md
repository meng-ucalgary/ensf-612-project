COMMUNICATION BETWEEN CONTROLLERS IN ANGULARJS ($EMIT, $ON)


AngularJS applications may need to communicate across the controllers. Such a communication might be needed to send notifications or to pass data between the controllers.
Although there can be different approaches to achieve this goal, one that is readily available is the event system of $scope and $rootScope. Both of these objects - $scope and 
$rootScope - support three methods namely $broadcast(), $emit() and $on() that facilitate event driven publisher-subscriber model for sending notifications and passing data 
between the controllers. In this article I will discuss how to raise events using $emit() and then how to handle those events using $on().

<div ng-app="TransportApp">
	<div ng-controller="VehicleCtrl">
		<div ng-controller="CarCtrl"></div>
		<div ng-controller="BusCtrl">
			<div ng-controller="BRTBusCtrl"></div>				
		</div>
	</div>
	<div ng-controller="TrainCtrl">
		<div ng-controller="LocalCtrl"></div>
		<div ng-controller="MetroCtrl"></div>
	</div>
	<div ng-controller="AirlineCtrl">
		<div ng-controller="PlaneCtrl"></div>
		<div ng-controller="HelicopterCtrl"></div>
	</div>
</div>

Now all controller register to TransportApp. Vehicle controller has two childs controller as Car controller and Bus controller which has child controller name as BRTBus controller. BRTBusCtrl controller raise event name as message with help of $emit. Events send a object ({ "message": "BRT Bus Controller Emit"} ) when the corresponding event is dispatched. You can easily substitute an string data instead of object. All controllers handle the event message and print a object in console by $on.
Ok. Now let's see the code of all the controllers mentioned above. 

	angular.module("TransportApp", [])

	.controller("VehicleCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : VehicleCtrl Recieved Message : " + object.message);
			});

		})
		.controller("CarCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : CarCtrl Recieved Message : " + object.message);
			});

		})
		.controller("BusCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : BusCtrl Recieved Message : " + object.message);
			});

		})
		.controller("BRTBusCtrl", function($scope, $rootScope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : BRTBusCtrl Recieved Message : " + object.message);
			});

			$scope.$emit("message",{
			  "message": "BRT Bus Controller Emit"
			});

		})
		.controller("TrainCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : TrainCtrl Recieved Message : " + object.message);
			});

		})
		.controller("LocalCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : LocalCtrl Recieved Message : " + object.message);
			});

		})
		.controller("MetroCtrl", function($scope, $rootScope) {
			$scope.$on("message", function(event, object) {
				console.log("Controller : MetroCtrl Recieved Message : " + object.message);
			});
			
		})
		.controller("AirlineCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : AirlineCtrl Recieved Message : " + object.message);
			});

		})
		.controller("PlaneCtrl", function($scope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : PlaneCtrl Recieved Message : " + object.message);
			});

		})
		.controller("HelicopterCtrl", function($scope, $rootScope) {

			$scope.$on("message", function(event, object) {
				console.log("Controller : HelicopterCtrl Recieved Message : " + object.message);
			});

		})

All controller handle the event message. Guess what should be result ? when we execute this example only three controller handle this event name as BRTBusCtrl, BusCtrl, Vehicle controller because as we discussed, the event raise by $emit, and that event should be handle by its parent controllers and itself as well. So other controller could not handle the event message.
Let's look at output:

Controller : BRTBusCtrlRecieved Message : BRT Bus Controller Emit 
Controller : BusCtrlRecieved Message : BRT Bus Controller Emit 
Controller : VehicleCtrlRecieved Message : BRT Bus Controller Emit

As above output , “BRT bus controller” string print on console which was raise by $emit by BRTBusCtrl controller.

Conclusion:

$emit raise the event and communicate between controllers. That communication sould be on parent child chain. If we need to share that event only in some controllers which are the parents of it then $emit  plays very important role. 
There are other methods also through which we can communicate between controllers. But this concept is very simple. It will be easier to understand, if you try to look at the examples one at a time...











