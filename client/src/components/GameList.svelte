<script lang="ts">
    import { onMount } from "svelte";

    interface Game {
        id: number;
        title: string;
        description: string;
        publisher_name?: string;
        category_name?: string;
    }

    export let games: Game[] = [];
    let loading = true;
    let error: string | null = null;

    const fetchGames = async () => {
        loading = true;
        try {
            const response = await fetch('/api/games');
            if(response.ok) {
                games = await response.json();
            } else {
                error = `Failed to fetch data: ${response.status} ${response.statusText}`;
            }
        } catch (err) {
            error = `Error: ${err instanceof Error ? err.message : String(err)}`;
        } finally {
            loading = false;
        }
    };

    onMount(() => {
        fetchGames();
    });
</script>

<div>
    <!-- Enhanced section header -->
    <div class="text-center mb-12">
        <h2 class="text-4xl font-bold mb-4 bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">Featured Games</h2>
        <p class="text-lg text-slate-400 max-w-2xl mx-auto">Discover the latest DevOps-inspired board games ready for funding</p>
        <div class="w-24 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mt-6 rounded-full"></div>
    </div>
    
    {#if loading}
        <!-- Enhanced loading animation -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {#each Array(6) as _, i}
                <div class="group bg-slate-800/60 backdrop-blur-sm rounded-2xl overflow-hidden shadow-xl border border-slate-700/50 hover:border-blue-500/50 transition-all duration-500">
                    <div class="p-8">
                        <div class="animate-pulse">
                            <!-- Card header -->
                            <div class="flex items-center justify-between mb-6">
                                <div class="h-3 bg-gradient-to-r from-slate-700 to-slate-600 rounded-full w-16"></div>
                                <div class="h-3 bg-gradient-to-r from-slate-700 to-slate-600 rounded-full w-8"></div>
                            </div>
                            <!-- Title -->
                            <div class="h-7 bg-gradient-to-r from-slate-700 to-slate-600 rounded-lg w-3/4 mb-4"></div>
                            <!-- Tags -->
                            <div class="flex gap-2 mb-6">
                                <div class="h-6 bg-gradient-to-r from-blue-900/60 to-blue-800/60 rounded-full w-20"></div>
                                <div class="h-6 bg-gradient-to-r from-purple-900/60 to-purple-800/60 rounded-full w-16"></div>
                            </div>
                            <!-- Description -->
                            <div class="space-y-3 mb-6">
                                <div class="h-4 bg-gradient-to-r from-slate-700 to-slate-600 rounded w-full"></div>
                                <div class="h-4 bg-gradient-to-r from-slate-700 to-slate-600 rounded w-5/6"></div>
                                <div class="h-4 bg-gradient-to-r from-slate-700 to-slate-600 rounded w-4/6"></div>
                            </div>
                            <!-- Progress bar -->
                            <div class="h-2 bg-slate-700 rounded-full w-full mb-4"></div>
                            <!-- Button -->
                            <div class="h-10 bg-gradient-to-r from-blue-600/60 to-purple-600/60 rounded-xl w-full"></div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    {:else if error}
        <!-- Enhanced error display -->
        <div class="text-center py-16 bg-gradient-to-br from-red-900/20 to-red-800/10 backdrop-blur-sm rounded-2xl border border-red-500/20">
            <div class="w-16 h-16 bg-red-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.996-.833-2.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z" />
                </svg>
            </div>
            <h3 class="text-xl font-semibold text-red-400 mb-2">Something went wrong</h3>
            <p class="text-red-300/80">{error}</p>
        </div>
    {:else if games.length === 0}
        <!-- Enhanced no games display -->
        <div class="text-center py-16 bg-gradient-to-br from-slate-800/40 to-slate-700/20 backdrop-blur-sm rounded-2xl border border-slate-700/50">
            <div class="w-16 h-16 bg-blue-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
            </div>
            <h3 class="text-xl font-semibold text-slate-300 mb-2">No games available</h3>
            <p class="text-slate-400">Check back soon for exciting new DevOps board games!</p>
        </div>
    {:else}
        <!-- Enhanced game list -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8" data-testid="games-grid">
            {#each games as game (game.id)}
                <a 
                    href={`/game/${game.id}`} 
                    class="group block relative bg-slate-800/60 backdrop-blur-sm rounded-2xl overflow-hidden shadow-xl border border-slate-700/50 hover:border-blue-500/50 hover:shadow-2xl hover:shadow-blue-500/10 transition-all duration-500 hover:transform hover:scale-[1.02] hover:-translate-y-2"
                    data-testid="game-card"
                    data-game-id={game.id}
                    data-game-title={game.title}
                >
                    <!-- Hover gradient overlay -->
                    <div class="absolute inset-0 bg-gradient-to-br from-blue-600/10 via-purple-600/5 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-500"></div>
                    
                    <!-- Animated background elements -->
                    <div class="absolute top-4 right-4 w-20 h-20 bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-full blur-xl opacity-0 group-hover:opacity-100 transition-all duration-700"></div>
                    
                    <div class="p-8 relative z-10">
                        <!-- Card header with status indicator -->
                        <div class="flex items-center justify-between mb-6">
                            <div class="flex items-center gap-2">
                                <div class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                                <span class="text-xs font-medium text-green-400 uppercase tracking-wider">Active</span>
                            </div>
                            <div class="w-8 h-8 bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-lg flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                                </svg>
                            </div>
                        </div>

                        <!-- Enhanced title -->
                        <h3 class="text-2xl font-bold text-slate-100 mb-4 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-400 group-hover:to-purple-400 group-hover:bg-clip-text transition-all duration-300" data-testid="game-title">
                            {game.title}
                        </h3>
                        
                        <!-- Enhanced tags -->
                        {#if game.category_name || game.publisher_name}
                            <div class="flex flex-wrap gap-2 mb-6">
                                {#if game.category_name}
                                    <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-gradient-to-r from-blue-900/60 to-blue-800/60 text-blue-300 border border-blue-700/30 group-hover:from-blue-800/80 group-hover:to-blue-700/80 transition-all duration-300" data-testid="game-category">
                                        {game.category_name}
                                    </span>
                                {/if}
                                {#if game.publisher_name}
                                    <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-gradient-to-r from-purple-900/60 to-purple-800/60 text-purple-300 border border-purple-700/30 group-hover:from-purple-800/80 group-hover:to-purple-700/80 transition-all duration-300" data-testid="game-publisher">
                                        {game.publisher_name}
                                    </span>
                                {/if}
                            </div>
                        {/if}
                        
                        <!-- Enhanced description -->
                        <p class="text-slate-400 mb-6 text-sm leading-relaxed line-clamp-3 group-hover:text-slate-300 transition-colors duration-300" data-testid="game-description">
                            {game.description}
                        </p>
                        
                        <!-- Funding progress (simulated) -->
                        <div class="mb-6">
                            <div class="flex justify-between text-xs text-slate-400 mb-2">
                                <span>Funding Progress</span>
                                <span>72%</span>
                            </div>
                            <div class="w-full bg-slate-700/50 rounded-full h-2 overflow-hidden">
                                <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500 rounded-full transition-all duration-1000 group-hover:shadow-lg group-hover:shadow-blue-500/30" style="width: 72%"></div>
                            </div>
                        </div>
                        
                        <!-- Enhanced call-to-action -->
                        <div class="flex items-center justify-between">
                            <div class="text-sm">
                                <div class="text-slate-400">Goal: <span class="text-white font-semibold">$25,000</span></div>
                                <div class="text-blue-400 font-semibold">$18,000 raised</div>
                            </div>
                            <div class="flex items-center text-sm text-blue-400 font-semibold group-hover:text-blue-300 transition-colors duration-300">
                                <span>View Details</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-2 transform transition-all duration-300 group-hover:translate-x-2 group-hover:scale-110" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Bottom gradient accent -->
                    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-500 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                </a>
            {/each}
        </div>
    {/if}
</div>