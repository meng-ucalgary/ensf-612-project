# Xamarin-Navy

Light weight starter template realized with Xamarin and Xamarin Forms with navigators implemented. The NavigatorService that handles the whole navigation in the app is implemented as a singleton and has to be initialised in App.xaml.cs.
## Work in progress
### Prerequisites

You just need any bootstrap app template from Xamarin. In Visual Studio 2017, file -> project -> new -> Cross Platform App (Xamarin Forms or Native). At this point you will have a project set up for you.

### Installing

This will probably be a nuget package, i suppose. So instructios on how to install the nuget package in the PCL would be nice.

```
Give the example
```

### Get it running

In App.xaml.cs, initiate the navigation service in the App() constructor:

```C#
var navigationService = new NavigationService();
```

At this point, you just need to instantiate the navigator you want passing it the initial page you want to display (here we suppose it's called FirstPage). It is necessary to include **also this call in the App() constructor** because it will set the **MainPage** of the app - otherwise you will get an exception for not having set the root page.

### Hierarchical Navigation
Navigate through pages, forwards and backwards, as desired. Push and pop pages from the navigation stack.
For having this kind of navigator, just add:

```C#
MainPage = navigationService.Initialize(new FirstPage());
```

### Tabs
Instead, for a TabbedPage Navigation add:

```C#
MainPage = navigationService.InitializeTabs(new List<CustomMenuItem> {
                new CustomMenuItem { TargetType = typeof(AboutPage), Title = "About", Icon = "tab_about.png" },
                new CustomMenuItem { TargetType = typeof(ItemsPage), Title = "Browse", Icon = "tab_feed.png" },
            });
```
where the `CustomMenuItem` represents a tab with his page to display, title and icon to show. It is possible to have till 5 tabs.

### Drawer (MasterDetailPage)
To have a drawer menu, use the implementation of the MasterDetailPage. This takes as arguments the drawer menu page and the first detail page to be displayed.

```C#
MainPage = navigationService.InitializeDrawer(new DrawerPage(), new FirstPage());
```

### Push Pages

#### Hierarchical Navigation (and Tabs)
```C#
Task PushView(Page page, ViewTransitionArgs transArgs, object args = null)
```

In case you wanna push a **modal** page, just add it as transArgs:
```C#
await PushView(page, new ViewTransitionArgs{IsModal:true})
```

#### MasterDetail Navigation

In this case the page gets pushed as DetailPage, the MasterPage will be indeed the drawer menu.

```C#
Task PushDetailView(Page page, object args = null)
```

Then, the DetailPage can be a navigationPage so we can hierachically push other pages on it to navigate forwards and backwards.



List with all the APIs


### ToDo:
- Set MainPage in NavigatorService for all the possible navigators
- Delete BaseMasterDetailPage (why is it even there?)
- Support code to combine navigators in one page
- Issue with iOS 7+: if i swipe from the edge the page pops, if i swipe from half the drawer gets shown
