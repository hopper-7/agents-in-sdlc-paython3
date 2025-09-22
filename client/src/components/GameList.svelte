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
    <div class="text-center mb-8">
        <h2 class="text-3xl font-bold mb-4">
            <span class="gradient-text">Featured Games</span>
        </h2>
        <div class="w-24 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-emerald-500 mx-auto rounded-full"></div>
    </div>
    
    {#if loading}
        <!-- Enhanced loading animation -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {#each Array(6) as _, i}
                <div class="glass-card rounded-2xl overflow-hidden shadow-2xl">
                    <div class="p-6">
                        <div class="animate-pulse">
                            <div class="h-6 shimmer-bg rounded-lg w-3/4 mb-4"></div>
                            <div class="h-4 shimmer-bg rounded w-1/2 mb-4"></div>
                            <div class="space-y-3 mb-6">
                                <div class="h-3 shimmer-bg rounded w-full"></div>
                                <div class="h-3 shimmer-bg rounded w-5/6"></div>
                                <div class="h-3 shimmer-bg rounded w-4/6"></div>
                            </div>
                            <div class="h-2 shimmer-bg rounded-full w-full mb-4"></div>
                            <div class="h-10 shimmer-bg rounded-xl w-1/3"></div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    {:else if error}
        <!-- Enhanced error display -->
        <div class="text-center py-16">
            <div class="glass-card rounded-2xl border border-red-500/30 p-8 max-w-md mx-auto">
                <div class="text-6xl mb-4">🚫</div>
                <h3 class="text-xl font-semibold text-red-400 mb-2">Oops! Something went wrong</h3>
                <p class="text-slate-300">{error}</p>
                <button on:click={fetchGames} class="mt-4 btn-primary text-white font-medium py-2 px-6 rounded-lg">
                    Try Again
                </button>
            </div>
        </div>
    {:else if games.length === 0}
        <!-- Enhanced no games display -->
        <div class="text-center py-16">
            <div class="glass-card rounded-2xl p-8 max-w-md mx-auto">
                <div class="text-6xl mb-4">🎮</div>
                <h3 class="text-xl font-semibold text-slate-200 mb-2">No Games Found</h3>
                <p class="text-slate-400">No games available at the moment. Check back soon!</p>
            </div>
        </div>
    {:else}
        <!-- Enhanced game cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8" data-testid="games-grid">
            {#each games as game, index (game.id)}
                <a 
                    href={`/game/${game.id}`} 
                    class="group block glass-card rounded-2xl overflow-hidden shadow-2xl hover:shadow-blue-500/20 hover:shadow-2xl transition-all duration-500 hover:translate-y-[-8px] hover:scale-[1.02] fade-in-up"
                    data-testid="game-card"
                    data-game-id={game.id}
                    data-game-title={game.title}
                    style="animation-delay: {index * 0.1}s;"
                >
                    <!-- Card glow effect on hover -->
                    <div class="absolute inset-0 bg-gradient-to-r from-blue-600/0 via-purple-600/0 to-emerald-600/0 group-hover:from-blue-600/20 group-hover:via-purple-600/20 group-hover:to-emerald-600/20 transition-all duration-500 rounded-2xl"></div>
                    
                    <div class="p-8 relative z-10">
                        <!-- Decorative corner element -->
                        <div class="absolute top-4 right-4 w-12 h-12 bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-full blur-xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        
                        <div class="relative">
                            <h3 class="text-xl font-bold text-slate-100 mb-4 group-hover:gradient-text transition-all duration-300" data-testid="game-title">
                                {game.title}
                            </h3>
                            
                            {#if game.category_name || game.publisher_name}
                                <div class="flex flex-wrap gap-2 mb-4">
                                    {#if game.category_name}
                                        <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-gradient-to-r from-blue-500/20 to-blue-600/20 text-blue-300 border border-blue-500/30" data-testid="game-category">
                                            {game.category_name}
                                        </span>
                                    {/if}
                                    {#if game.publisher_name}
                                        <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-gradient-to-r from-purple-500/20 to-purple-600/20 text-purple-300 border border-purple-500/30" data-testid="game-publisher">
                                            {game.publisher_name}
                                        </span>
                                    {/if}
                                </div>
                            {/if}
                            
                            <p class="text-slate-400 mb-6 text-sm leading-relaxed line-clamp-3" data-testid="game-description">
                                {game.description}
                            </p>
                            
                            <!-- Enhanced call-to-action -->
                            <div class="mt-6 flex items-center justify-between">
                                <div class="text-sm font-semibold text-blue-400 flex items-center group-hover:text-blue-300 transition-colors">
                                    <span>View Details</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-2 transform transition-transform duration-300 group-hover:translate-x-2" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                    </svg>
                                </div>
                                
                                <!-- Progress indicator -->
                                <div class="w-16 h-2 bg-slate-700/50 rounded-full overflow-hidden">
                                    <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500 rounded-full transform transition-transform duration-700 group-hover:translate-x-0 -translate-x-full"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Bottom accent line -->
                    <div class="h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-emerald-500 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-left"></div>
                </a>
            {/each}
        </div>
    {/if}
</div>