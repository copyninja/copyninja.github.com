---
layout: post
title: "Update: Falcon Debian package Status"
tags:
 - Debian
 - packaging
---

Recently I wrote about packaging Falcon programming language for Debian. So here
is the status of package.
Package builds multiple binaries and we have successfully separated modules from core
Falcon language component

1. falconpl (Falcon language itself )
2. falconpl-dbg (Debug symbols)
3. libfalconpl-engine1 (Falcon engine library)
4. libfalconpl-engine1-dbg (Debug symbols for Falcon enging)

Core modules like *feathers*  and modules writtein *Falcon* itself are part of *libfalconpl-engine1*.
Rest of modules are separated into following packages

1. falconpl-mongodb: Mongodb connector module
2. falconpl-dbi : Database Abstraction layer
3. falconpl-dbi-sqlite3: SQLite3 connector based on DBI module
4. falconpl-dbi-postgresql: PostgreSQL connector based on DBI module
5. falconpl-dbi-mysql: MySQL connector based on DBI module
6. falconpl-dbi-firebird: Firebird DB server connector
7. falconpl-curl: Curl bindings for Falcon
8. falconpl-dbus: DBus bindings for Falcon
9. falconpl-dmtx: Data Matrix reader/writer for Falcon
10. falconpl-hpdf: Haru based PDF module for Falcon
11. falconpl-gd2: Graphic manipulation module for Falcon

There are 4 modules which I'm not sure how to build (dependency) or if at all possible to build for Linux
they are *dynlib, wopi, sdl, conio*. I need to consult upstream on these modules status and ability to build.

## Modules not built ##
We didn't build *dbi-oracle* and *dbi-odbc* modules as these are proprietary software dependant. Additionally 
in a conversation with upstream on IRC it was told *dynlib* module can't be built for 64bit and X86 version
of Linux because lack of assembler, but I've not fully confirmed this.

## Legal Issues ##
To enable the *curl* bindings I added curl dependency which in turn has dependency on *libssl1.0* library which
is part of *openssl* source package which is causing lintian thrown on GPL violation error. Kartik will be looking
into this.

## Patches submitted ##
I've submitted total of [6 patches](http://anonscm.debian.org/gitweb/?p=collab-maint/falconpl.git;a=tree;f=debian/patches;h=aac74cd0c32cb33662cf6f6fd5f4b249c708d77a;hb=HEAD) of which 5 patches are already applied to upstream git repo and 6th one is waiting to be applied. In other
words upstream is really helpful to us.

Well thats all for this week more updates next week (or may be even before that ;-) )
