# Plugins for Unity With Android Google Play

> related date : 2024-01-23

## What did I do?

* ~~Unity 2020.2.5f1~~ Unity 2022+ LTS
* `python3 install-plugins.py`
* ~~Go to `Google` -> `Play Billing` -> `Build Settings`, If Console Show Errors About `DirectoryNotFoundException: Could not find a part of the path '/Users/Shared/Github/jewel/unity/Assets/Plugins/UnityPurchasing/Bin/Android'.`, Create Directory `Assets/Plugins/UnityPurchasing/Bin/Android` Manually. Reopen `Build Settings` to Check Again.~~
* Google Billing Plugin is Outdated, Use Unity IAP Instead <https://docs.unity3d.com/Packages/com.unity.purchasing@4.10/manual/UnityIAPGoogleConfiguration.html>
* `Services` -> `Explore` Link Project and Configure  `Google Play Configuration`
* `Assets` -> `External Dependency Manager` -> `Android Resolver` -> `Force Resolve`
* Go to `https://analytics.google.com/`, Download `google-services.json` to `Assets/Plugins/Android`
* Go to `Edit` -> `Project Settings` -> `Player` -> `Android` -> `Publishing Settings` -> `Build`, Check All `Custom X` is On.
* Change Template `classpath 'com.android.tools.build:gradle:4.0.1'` in `Assets/Plugins/Android/baseProjectTemplate.gradle` to `classpath 'com.android.tools.build:gradle:7.1.2'` (for Unity 2022+, use gradle 7.1.2 <https://docs.unity3d.com/Manual/android-gradle-overview.html>)
* ~~`File` -> `Build Settings` -> `Android` Check `Export Project` And `Export for App Bundle`~~
* ~~Build It, Open `Android Studio` to Build `APK` or `AAB`~~
* `Google` -> `Build Android App Bundle` -> `Done`

## Used Plugins

> Plugins for Unity Can Be Downloaded Here <https://developers.google.com/unity/packages>

* AdMob Unity Plugin, For Ad Support
  * <https://developers.google.com/admob/unity/quick-start>
  * <https://github.com/googleads/googleads-mobile-plugins/releases/latest>
<https://github.com/googleads/googleads-mobile-unity/releases/download/v8.6.0/GoogleMobileAds-v8.6.0.unitypackage>

* Android App Bundle - For Export Android App Bundle
<https://dl.google.com/games/registry/unity/com.google.android.appbundle/com.google.android.appbundle-1.9.0.unitypackage>

* Firebase Crashlytics - Crash Reporting
<https://dl.google.com/firebase/sdk/unity/dotnet4/FirebaseCrashlytics_11.6.0.unitypackage>

* Google Analytics
<https://dl.google.com/firebase/sdk/unity/dotnet4/FirebaseAnalytics_11.6.0.unitypackage>

* Play Asset Delivery - For Package Larger Than 150MB Package Can Split Into Multiple Packages
<https://dl.google.com/games/registry/unity/com.google.play.assetdelivery/com.google.play.assetdelivery-1.8.2.unitypackage>

* Play Billing Library - For In-App Purchase Support, But this plugin is out dated, use Unity IAP instead
~~<https://dl.google.com/games/registry/unity/com.google.play.billing/com.google.play.billing-3.2.4.unitypackage>~~

* Play In-App Review
<https://dl.google.com/games/registry/unity/com.google.play.review/com.google.play.review-1.8.1.unitypackage>

* Play In-App Update
<https://dl.google.com/games/registry/unity/com.google.play.appupdate/com.google.play.appupdate-1.8.1.unitypackage>

* External Dependency Manager for Unity
<https://github.com/googlesamples/unity-jar-resolver/raw/v1.2.177/external-dependency-manager-1.2.177.unitypackage>
