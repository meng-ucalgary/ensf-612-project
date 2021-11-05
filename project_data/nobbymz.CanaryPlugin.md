## Summary

The CanaryPlugin project is a template for creating a new project for the CanaryMod server implementation for Minecraft. It can compile out of box, but will do absolutely nothing without modification.

**Do not use the me.sgray namespace! Change to either use either an email account or domain name that YOU own.**

## Motivation

There's a lot of examples of how to create a pom.xml file for Maven-enabled projects, but very few designed to give a basis for CanaryMod plugins. The pom.xml in this project contains the most relevant and useful properties to someone creating a new plugin, including the necessary dependency on the CanaryMod API.

## Installation

Clone this git repository into your Eclipse workspace and go to create a new Java project. Eclipse should automatically detect the settings provided by this project and create anything missing. You will need to enable the Maven nature, easy as right-clicking the project root in Package Explorer, hovering "Configure", and clicking "Convert to Maven Project".

Additionally,

1. Rename the me.sgray.template.canaryplugin package to reflect your own namespace. (tld.yourdomain.whatever)
2. Edit the pom.xml to reflect your project properties. Work slowly through this if you are still new to using Maven. A great reference about the available properties is at http://maven.apache.org/ref/3.2.3/maven-model/maven.html
3. Basic settings in Canary.inf are handled with Maven property filters, notable by the ${property} syntax. Additional settings can be added if needed at Canary.inf though.

## Troubleshooting

**Eclipse says "Plugin cannot be resolved to a type" when extending the Canary API**

Make sure you have the Maven nature enabled. Otherwise Eclipse won't know to read the pom.xml

**Plugin doesn't compile with error like "Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.1:compile (default-compile) on project CanaryPlugin: Compilation failure**
**No compiler is provided in this environment. Perhaps you are running on a JRE rather than a JDK?"**

Providing you *do* have the Java JDK installed and you're certain your system knows where to find it, just right-click the project in Package Explorer, hover "Maven", and click "Update Project". This is highly likely to resolve the matter.

## Make This Your Own

Feel free to (and please do) clone this project and make adjustments to fit your needs/preferences.

## CanaryMod Resources

Official website: http://canarymod.net/

Javadocs: https://ci.visualillusionsent.net/job/CanaryLib/javadoc/

## Credits

* Kudos to Oracle for the Eclipse IDE and Apache for Maven.
* Thank you to the CanaryMod community for building a great API and having a friendly community

## License

Zlib was chosen as the basis for this project (CanaryPlugin) as it is highly permissive and easy for people to understand. The license has only been modified for this project to reflect authorship and creation year.

Copyright (c) 2014 Shaila Gray

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
claim that you wrote the original software. If you use this software
in a product, an acknowledgment in the product documentation would be
appreciated but is not required.

2. Altered source versions must be plainly marked as such, and must not be
misrepresented as being the original software.

3. This notice may not be removed or altered from any source
distribution.