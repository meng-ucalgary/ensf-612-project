# MaterialWidget

Android Lollipop design widget in Android 4.0 ~ 4.4.

##Widget

####Button

######Paper Button

![paper button](capture/paper_button.png)
```xml
<com.material.widget.PaperButton
    widget:paper_text="Paper Button"
    android:layout_width="160dp"
    android:layout_height="54dp"/>
```

######Circle Button

![circle button](capture/circle_button.png)
```xml
<com.material.widget.CircleButton
    android:id="@+id/circle_button"
    widget:circle_icon="@drawable/ic_add"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

####Indicator

######Tab Indicator

![tab indicator](capture/tab_indicator.png)
```xml
<com.material.widget.TabIndicator
    android:id="@+id/indicator"
    android:background="@color/primary_color"
    android:layout_width="match_parent"
    android:layout_height="50dp"/>
```

####EditText

######Floating EditText

![floating edit text](capture/floating_edit_text.png)
```xml
<com.material.widget.FloatingEditText
    android:hint="FloatingEditText"
    android:layout_marginLeft="40dp"
    android:layout_marginRight="40dp"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"/>
```

####ProgressBar

######Circular Progress

![circular progress](capture/circular_progress.png)
```xml
<com.material.widget.CircularProgress
    android:layout_marginTop="10dp"
    widget:circular_progress_size="Normal"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

####CompoundWidget

######Switch

![switch](capture/switch.png)
```xml
<com.material.widget.Switch
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

######Radio Button

![radio button](capture/radio_button.png)
```xml
<com.material.widget.RadioButton
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

######Check Box

![check box](capture/check_box.png)
```xml
<com.material.widget.CheckBox
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

