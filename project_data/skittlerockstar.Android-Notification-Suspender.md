# Android-Notification-Suspender
Cancels out all notifications. When stopped, re-initiates all suspended notifications. 

**Only for Android N+ because of a bug that disconnects the service on lower API's.**  
See: https://issuetracker.google.com/issues?q=notificationlistenerservice

## Step 1 : Files 

The following files are necessary :
* NotificationSuspender.java
* NotificationSuspenderManager.java
* layout/empty_heads_up_view.xml
* values/notification_suspender_values.xml

## Step 2 : Manifest
To make the NotificationSuspender work, the following service needs to be added to the manifest:  

        <service android:name=".NotificationSuspender"
            android:permission="android.permission.BIND_NOTIFICATION_LISTENER_SERVICE">
            <intent-filter>
                <action android:name="android.service.notification.NotificationListenerService" />
            </intent-filter>
        </service>
        
Also the following permissions are needed:

         <uses-permission android:name="android.permission.ACCESS_NOTIFICATION_POLICY" />
         <uses-permission android:name="android.permission.BIND_NOTIFICATION_LISTENER_SERVICE"/>
         <uses-permission android:name="android.permission.VIBRATE"/> 
         <!-- headsup-cancellation will not work without VIBRATE permission -->
## Step 3 : Usage

### 3.1 Adding an exception
**values/notification_suspender_values.xml** contains a string-array for packages that need to be ignored:  
```
<string-array name="exceptions">
        <item>com.android.dialer</item>
        <item>com.android.incallui</item>
</string-array>
```
The packages in this array will be ignored by the notification suspender.  
By default, the application that runs this notification suspender is an exception as well.

**SUPPORT FOR ADDING RUNTIME EXCEPTIONS IN PROGRESS!**

### 3.2 Checking permission.

To check if the user has given permission use :
```
boolean userHasGivenPermission = NotificationSuspenderManager.hasPermission(activity);
```

To ask for permission, use:
``` 
NotificationSuspenderManager.askPermission(activity); 
```
Then use an onActivityResult to check the result:
```
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if(requestCode == NotificationSuspenderManager.NOTIFICATION_ACCESS_REQUESTCODE 
                && NotificationSuspender.isServiceRunning()){
            //Permission granted and Service is running! ( not yet enabled )
        }
        super.onActivityResult(requestCode, resultCode, data);
    }
```

### 3.3 Using the service
Last but not least, you can do 3 things in Version 0.1 :

* Enable the service - Use ```NotificationSuspenderManager.enable(context);```  
  - enables notification suspention.
* Disable the service - Use ```NotificationSuspenderManager.disable(context);```  
  - disables notification suspention ( previously suspended notifications aren't removed! )
* Revive the suspended notifications - Use ```NotificationSuspenderManager.revive(context);```  
  - disables notification suspention AND revives all previously suspended notifications.
