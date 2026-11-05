---
name: mobile-release
description: "Pre-release checklist for iOS and Android apps (React Native/Expo, Flutter, native). Use before submitting a build to the App Store or Google Play."
---

Check each item and report PASS / FAIL / N/A with evidence (file path or command output). Do not change signing or store settings; report instead.

## Versioning
- Version name and build number bumped (iOS `CFBundleShortVersionString` / `CFBundleVersion`, Android `versionName` / `versionCode`, or `app.json` / `pubspec.yaml`).

## Build
- Release build succeeds for both platforms (e.g. `eas build`, `flutter build ipa/appbundle`, `xcodebuild archive`, `./gradlew bundleRelease`).
- No debug flags, dev URLs, or test API keys in release config.

## Permissions and privacy
- Every permission has a usage description (iOS `NS*UsageDescription`) and is actually needed.
- iOS privacy manifest (`PrivacyInfo.xcprivacy`) present when required; Android data safety info up to date.

## Security
- Tokens stored in Keychain / Keystore / secure storage only.
- No secrets in the bundle; HTTPS only (ATS / network security config not weakened).
- Android: release is minified/obfuscated if the project uses R8/ProGuard.

## Quality
- Tests pass; no crash on cold start, offline start, or after backgrounding.
- Deep links and push notifications work in a release build.
- App icon, splash screen, and store screenshots are current.

End with a go / no-go verdict and the list of FAIL items.
