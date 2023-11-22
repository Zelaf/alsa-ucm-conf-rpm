# Updated ALSA UCM configurations for Fedora

This is a spec file for fedora that's configured to create a package for a commit archive of the [ALSA UCM configurations](https://github.com/alsa-project/alsa-ucm-conf/) GitHub repository.

This will allow you to use audio cards and audio interfaces more seamlessly with Linux.

To check if there's a profile for your audio interface, look for yours in the ALSA UCM repository.

## Installation
I maintain RPM packages [through Copr](https://copr.fedorainfracloud.org/coprs/zelaf/alsa-ucm/). The Copr repository is currently a WIP and will be cleaned up soon.

To create your own RPM package locally, you can follow the guide [here](https://rpm-packaging-guide.github.io/#packaging-software)

## How does UCM configurations work?
When ALSA detects a device it checks through a configuration file if that device has any configuration profiles available by looking at some information pointers of the connected device.

It uses that configuration profile to see how many inputs and outputs it has as well as if it should be stereo, mono, etc.

## How do I make new profiles?
If you have an audio device not included in the ALSA UCM GitHub repository feel free to make your own. If you have a similar device you can compare how it looks and what to change.

@brndd made a pretty solid guide [here](https://gist.github.com/brndd/ccec98a575f7c0422d50402937439227).

Feel free to make a commit to alsa-ucm-conf to have it reviewed and added.

Alternatively you can fork this repo and the alsa-ucm-conf repo and change `Source0` to the tarball of your alsa-ucm-conf repo. This is however only needed if you need an RPM package. If you don't need an RPM package you can just follow the `curl` and `tar` command in the ALSA UCM repo.

## Contributing
**Please do.** This is my first RPM package and I'm sure that there are a bunch of things I could clean up and make better.

As for my plans I think I'm gonna create two packages called `alsa-ucm` and `alsa-ucm-git` where the `git` gets done automatically when there's a new commit. While I cannot personally test the devices in the UCM configurations, installation and build errors can be rectified.

Currently I need help on finding better ways to rectify package conflicts and file conflicts with the original `alsa-ucm` package.

If you have any pointers or ideas please open an issue or make a PR!

## Big thanks
This wouldn't have been started without the help of @KyleGospo! Their help did me wonders in troubleshooting and working it out!

This is also forked and edited from [OpenMandrivaAssociation/alsa-ucm-conf](https://github.com/OpenMandrivaAssociation/alsa-ucm-conf) which gave me a great starting point!

And a huge thanks to the contributers and maintainers of [alsa-project/alsa-ucm-conf](https://github.com/alsa-project/alsa-ucm-conf/) for expanding on the UCM configurations to make it better!