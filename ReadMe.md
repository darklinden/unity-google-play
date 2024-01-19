# Deal With Plugins for Unity

## What did I do?

* Unity 2020.2.5f1
* `python3 install-plugins.py`
* Go to `Google` -> `Play Billing` -> `Build Settings`, If Console Show Errors About `DirectoryNotFoundException: Could not find a part of the path '/Users/Shared/Github/jewel/unity/Assets/Plugins/UnityPurchasing/Bin/Android'.`, Create Directory `Assets/Plugins/UnityPurchasing/Bin/Android` Manually. Reopen `Build Settings` to Check Again.
* `Assets` -> `External Dependency Manager` -> `Android Resolver` -> `Force Resolve`
* Go to `https://analytics.google.com/`, Download `google-services.json` to `Assets/Plugins/Android`
* Go to `Edit` -> `Project Settings` -> `Player` -> `Android` -> `Publishing Settings` -> `Build`, Check All `Custom X` is On.
* Change Template `classpath 'com.android.tools.build:gradle:4.0.1'` in `Assets/Plugins/Android/baseProjectTemplate.gradle` to `classpath 'com.android.tools.build:gradle:4.2.1'`
* `File` -> `Build Settings` -> `Android` Check `Export Project` And `Export for App Bundle`
* Build It, Open `Android Studio` to Build `APK` or `AAB`

## Used Plugins

<https://developers.google.com/unity/packages>

* Google AdMob

> GoogleMobileAds-v8.6.0.unitypackage

* Android App Bundle

> com.google.android.appbundle-1.9.0.unitypackage

* Android Performance Tuner

> android-performance-tuner-1.1.2.unitypackage

* Firebase Crashlytics

> FirebaseCrashlytics_11.6.0.unitypackage

* Google Analytics

> FirebaseAnalytics_11.6.0.unitypackage

* Play Asset Delivery

> com.google.play.assetdelivery-1.8.2.unitypackage

* Play Billing Library

> com.google.play.billing-3.2.4.unitypackage

* Play In-App Review

> com.google.play.review-1.8.1.unitypackage

* Play In-App Update

> com.google.play.appupdate-1.8.1.unitypackage

* External Dependency Manager for Unity

> external-dependency-manager-1.2.177.unitypackage
